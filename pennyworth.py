import sys, os

from src.database import *
from src.moveFile import move_file
from src.ruleItem import RuleItem
from src.addRuleDialog import AddRuleDialog
from src.ruleModel import RuleModel
from src.deleteDialog import DeleteDialog
from src.database import SQLDatabase

from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QDialog, 
    QListWidgetItem,
    QSystemTrayIcon,
    QMenu
)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QAction, QIcon

from ui.ui_mainwindow import Ui_MainWindow

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

basedir = os.path.dirname(__file__)

try:
    from ctypes import windll

    myappid = "remosrulloda.pennyworth.subproduct.0"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = RuleModel()
        self.setWindowTitle("Pennyworth")

        # Create and load database
        self.db = SQLDatabase()
        self.db.loadDataFromDB()

        # UI version
        self.loadDataFromDB()   

        # Connecting buttons
        self.addRuleBtn.pressed.connect(self.addRule)
        self.deleteRuleBtn.pressed.connect(self.deleteRule)

        # Set up QTimer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.run_all_rules)
        self.timer.start(1000)

        self.rules_paused = False

        self.init_tray()

    def init_tray(self):
        self.tray_icon = QSystemTrayIcon(QIcon(os.path.join(basedir, "icons/pennyworth.ico")), self)
        self.tray_icon.setVisible(True)

        tray_menu = QMenu(self)

        self.tray_icon.activated.connect(self.activate)

        self.tray_icon.showMessage(
            "Pennyworth", "Pennyworth is running in the system tray", QSystemTrayIcon.Information, 3000
        )

        self.trayPauseAction = QAction("Pause", self)
        self.trayPauseAction.triggered.connect(self.pauseRules)
        tray_menu.addAction(self.trayPauseAction)

        quitApp = QAction("Quit", self)
        quitApp.triggered.connect(QApplication.quit)
        tray_menu.addAction(quitApp)

        self.tray_icon.setContextMenu(tray_menu)

    def pauseRules(self):
        if self.rules_paused:
            self.timer.start(1000)
            self.trayPauseAction.setText("Pause")
        else:
            self.timer.stop()
            self.trayPauseAction.setText("Resume")
        
        self.rules_paused = not self.rules_paused


    def addRule(self):
        # Add a rule to the rule file rules list 
        dialog = AddRuleDialog()

        if dialog.exec():
            rule_data = dialog.getRuleData()
            if rule_data:
                self.updateUIWithNewRule(rule_data)

                # Insert into database
                self.db.insertRuleIntoDB(rule_data)

    def editRule(self, item, current_rule_data):
        dialog = AddRuleDialog()
        dialog.setRuleData(current_rule_data)

        if dialog.exec():
            updated_rule_data = dialog.getRuleData()
            updated_rule_data['uuid'] = current_rule_data['uuid']

            # Update rule in database
            self.db.updateRuleInDB(updated_rule_data)

            # Update the model
            index = self.model.rules.index(current_rule_data)
            self.model.rules[index] = updated_rule_data

            # Updates the QListWidget item with new data
            item.setData(Qt.UserRole, updated_rule_data)

            # Updated widget UI
            rule_widget = self.ruleView.itemWidget(item)
            rule_widget.ui.rule.setText(updated_rule_data['ruleName'])
            rule_widget.rule_data = updated_rule_data


        
    def deleteRule(self):
        selected_indexes = self.ruleView.selectedItems()
        if not selected_indexes:
            return

        item = selected_indexes[0]
        rule_data = item.data(Qt.UserRole)

        print(f"Deleted {rule_data['ruleName']}")

        dialog = DeleteDialog(rule_data['ruleName'])

        if dialog.exec() == QDialog.Accepted:
            index = self.ruleView.row(item)
            self.model.beginRemoveColumns(self.model.index(index), index, index)
            del self.model.rules[index]
            self.model.endRemoveRows()

            self.ruleView.takeItem(self.ruleView.row(item))
            self.ruleView.clearSelection()

            # Delete rule from database
            self.db.deleteRuleFromDB(rule_data['uuid'])

    def getSelectedRuleData(self):
        selected_items = self.ruleView.selectedItems()
        if not selected_items:
            return None
        
        selected_item = selected_items[0]
        rule_data = selected_item.data(Qt.UserRole)
        return rule_data
    
    def run_all_rules(self):
        active_rules = self.getActiveRules()
        for rule in active_rules:
            try:
                move_file(
                    rule['comparisonOperator'],
                    rule['comparisonValue'],
                    rule['sourceDir'],
                    rule['destDir']
                )
            except Exception as e:
                print(f"Error applying rule {rule['ruleName']}: {e}")
    
    def loadDataFromDB(self):
        rules = self.db.loadDataFromDB()
        for rule in rules:
            self.updateUIWithNewRule(rule)

    def updateUIWithNewRule(self, rule_data):
        item = QListWidgetItem(self.ruleView)
        rule_widget = RuleItem(rule_data)
        rule_widget.editRequested.connect(lambda data, item=item: self.editRule(item, data))
        item.setData(Qt.UserRole, rule_data)
        item.setSizeHint(rule_widget.sizeHint())
        self.ruleView.addItem(item)
        self.ruleView.setItemWidget(item, rule_widget)
        self.model.addRule(rule_data)


    def closeEvent(self, event):
        self.timer.stop()
        self.db.closeDB()
        event.accept()

    def getActiveRules(self):
        active_rules = []

        for index in range(self.ruleView.count()):
            rule = self.ruleView.item(index)
            rule_widget = self.ruleView.itemWidget(rule)
            if rule_widget.isActive():
                active_rules.append(rule_widget.rule_data)

        return active_rules
    
    def activate(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.show()
            self.activateWindow()
            self.raise_()
    
if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon(os.path.join(basedir, "icons/pennyworth.ico")))
    window = MainWindow()
    app.setQuitOnLastWindowClosed(False)
    sys.exit(app.exec())