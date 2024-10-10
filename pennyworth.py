import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow, QFileDialog, QDialog
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QAbstractListModel

from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_addRule import Ui_Dialog

class AddRuleDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Add Rule")
        self.sourceDir = ''
        self.destDir = ''

        # Connecting buttons
        self.ui.sourceBtn.pressed.connect(self.addSourceDir)

    def addSourceDir(self):
        fileName = QFileDialog.getExistingDirectory()
        if fileName:
            self.sourceDir = fileName
            self.customChangeEvent(fileName)
            self.ui.folderSourceLabel.setText(fileName)

    def customChangeEvent(self, fileName):
        print(f"Directory changed to {fileName}")

    


class RuleModel(QAbstractListModel):
    def __init__(self, rules=None):
        super().__init__()
        self.rules = rules or []
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            status, text = self.rules[index.row()]
            return text
        
    def rowCount(self, index):
        return len(self.rules)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = RuleModel()
        self.ruleView.setModel(self.model)
        self.setWindowTitle("Pennyworth")

        # Connecting buttons
        self.addRuleBtn.pressed.connect(self.add)

    def add(self):
        # Add a rule to the rule file rules list 
        dialog = AddRuleDialog()
        if dialog.exec():
            rule_text = dialog.getRule()
            if rule_text:
                self.model.addRule(("active", rule_text))

    
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


# class TrayApp(QApplication):
#     def __init__(self, args):
#         super().__init__(args)
#         self.main_window = MainWindow()

#         # Create the system tray icon
#         self.tray_icon = QSystemTrayIcon(QIcon("icon.png"), self) 
#         self.tray_icon.setToolTip("Pennyworth")

#         # Create a context menu for the tray icon
#         tray_menu = QMenu()
#         open_action = QAction("Open", self)
#         open_action.triggered.connect(self.show_window)
#         exit_action = QAction("Exit", self)
#         exit_action.triggered.connect(self.exit_app)
#         settings_action = QAction("Settings", self)
#         settings_action.triggered.connect(self.exit_app)

#         tray_menu.addAction(open_action)
#         tray_menu.addAction(settings_action)
#         tray_menu.addAction(exit_action)

#         self.tray_icon.setContextMenu(tray_menu)
#         self.tray_icon.activated.connect(self.on_tray_icon_clicked)
#         self.tray_icon.show()

#     def show_window(self):
#         self.main_window.show()

#     def exit_app(self):
#         self.quit()

#     def on_tray_icon_clicked(self, reason):
#         # Handle click events for the tray icon
#         if reason == QSystemTrayIcon.Trigger: 
#             if not self.main_window.isVisible():
#                 self.main_window.show()
#             else:
#                 self.main_window.hide()
