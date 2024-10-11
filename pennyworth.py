import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow, QFileDialog, QDialog, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QAbstractListModel

from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_addRule import Ui_Dialog
from ui.ui_deleteRule import Ui_Dialog as delete_Dialog

class AddRuleDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Add Rule")

        # Rule members
        self.ruleName = ''
        self.sourceDir = ''
        self.destDir = ''
        self.fileAttribute = ''
        self.comparisonOperator = ''
        self.comparisonValue = ''
        self.actionToTake = ''

        # Connecting buttons
        self.ui.sourceBtn.pressed.connect(self.addSourceDir)
        self.ui.destBtn.pressed.connect(self.addDestDir)
        self.ui.confirmBtn.pressed.connect(self.addRule)
        self.ui.cancelBtn.pressed.connect(self.reject)

        self.ui.ruleNameEdit.textChanged.connect(lambda: self.onInputChange('ruleName'))
        self.ui.lineEdit.textChanged.connect(lambda: self.onInputChange('comparisonValue'))

    def onInputChange(self, fieldType):
        reset_styles = {
            'source': lambda: self.ui.folderSourceLabel.setStyleSheet("color: green;"),
            'dest': lambda: self.ui.destFolderLabel.setStyleSheet("color: green;"),
            'ruleName': lambda: self.ui.ruleNameEdit.setStyleSheet(""),
            'comparisonValue': lambda: self.ui.lineEdit.setStyleSheet("")
        }

        reset_style_func = reset_styles.get(fieldType)
        if reset_style_func:
            reset_style_func()

    def addSourceDir(self):
        sourceName = QFileDialog.getExistingDirectory()
        if sourceName:
            self.sourceDir = sourceName
            self.customChangeEvent(sourceName)
            self.ui.folderSourceLabel.setText(sourceName)
            self.onInputChange('source')

    def addDestDir(self):
        destName = QFileDialog.getExistingDirectory()
        if destName:
            self.destDir = destName
            self.customChangeEvent(destName)
            self.ui.destFolderLabel.setText(destName)
            self.onInputChange('dest')

    def customChangeEvent(self, fileName):
        print(f"Directory changed to {fileName}")

    def addRule(self):
        self.ruleName = self.ui.ruleNameEdit.text().strip()
        self.fileAttribute = self.ui.ruleComboBox.currentText().strip()
        self.comparisonOperator = self.ui.verbComboBox.currentText().strip()
        self.comparisonValue = self.ui.lineEdit.text().strip()
        self.actionToTake = self.ui.actionComboBox.currentText().strip()

        # Validate Inputs
        validation_map = {
            "Source Directory": self.sourceDir,
            "Destination Directory": self.destDir,
            "File Attribute": self.fileAttribute,
            "Comparison Operator": self.comparisonOperator,
            "Comparison Value": self.comparisonValue,
            "Action": self.actionToTake,
            "Name": self.ruleName
        }

        missing_fields = []

        for field_name, value in validation_map.items():
            if not value:
                missing_fields.append(field_name)

        if missing_fields:
            self.highlightMissingFields(missing_fields)
            return
    
        # Accept and return the rule
        self.accept()

    def highlightMissingFields(self, missing_fields):
        # Reset all field backgrounds to default color
        self.ui.ruleNameEdit.setStyleSheet("")
        self.ui.folderSourceLabel.setStyleSheet("")
        self.ui.destFolderLabel.setStyleSheet("")
        self.ui.lineEdit.setStyleSheet("")
        self.ui.verbComboBox.setStyleSheet("")
        self.ui.ruleComboBox.setStyleSheet("")
        self.ui.actionComboBox.setStyleSheet("")

        for field_name in missing_fields:
            if field_name == "Source Directory":
                self.ui.folderSourceLabel.setText("No Source Folder")
                self.ui.folderSourceLabel.setStyleSheet("background-color: rgba(255, 0, 0, 0.3);")  
            elif field_name == "Destination Directory":
                self.ui.destFolderLabel.setText("No Destination Folder")
                self.ui.destFolderLabel.setStyleSheet("background-color: rgba(255, 0, 0, 0.3);") 
            elif field_name == "File Attribute":
                self.ui.ruleComboBox.setStyleSheet("background-color: rgba(255, 0, 0, 0.3);") 
            elif field_name == "Comparison Operator":
                self.ui.verbComboBox.setStyleSheet("background-color: rgba(255, 0, 0, 0.3);") 
            elif field_name == "Comparison Value":
                self.ui.lineEdit.setStyleSheet("background-color: rgba(255, 0, 0, 0.3);") 
            elif field_name == "Action":
                self.ui.actionComboBox.setStyleSheet("background-color: rgba(255, 0, 0, 0.3);") 
            elif field_name == "Name":
                self.ui.ruleNameEdit.setStyleSheet("background-color: rgba(255, 0, 0, 0.3);") 

    def getRuleName(self):
        return f"{self.ruleName}"

    def showErrorMessage(self, message):
        QMessageBox.warning(self, "Input Error", message)


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
            
    def addRule(self, rule):
        self.beginInsertRows(self.index(len(self.rules)), len(self.rules), len(self.rules))
        self.rules.append(rule)
        self.endInsertRows()


class DeleteDialog(QDialog, delete_Dialog):
    def __init__(self, rule_name):
        super().__init__()
        self.ui = delete_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Delete Rule")
        self.ui.deleteMsgLabel.setText(f"Are you sure you want to delete the rule: '{rule_name}'?")

        # Connect buttons
        self.ui.confirmDeleteBtn.pressed.connect(self.confirmDelete)
        self.ui.cancelDeleteBtn.pressed.connect(self.reject)

    def confirmDelete(self):
        self.accept()
    

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = RuleModel()
        self.ruleView.setModel(self.model)
        self.setWindowTitle("Pennyworth")

        # Connecting buttons
        self.addRuleBtn.pressed.connect(self.add)
        self.deleteRuleBtn.pressed.connect(self.delete)

    def add(self):
        # Add a rule to the rule file rules list 
        dialog = AddRuleDialog()
        if dialog.exec():
            rule_text = dialog.getRuleName()
            if rule_text:
                self.model.addRule((True, rule_text))

    def delete(self):
        indexes = self.ruleView.selectedIndexes()
        if indexes:            
            index = indexes[0]
            rule_name = self.model.rules[index.row()][1]
            dialog = DeleteDialog(rule_name)
            if dialog.exec():
                del self.model.rules[index.row()]
                self.model.layoutChanged.emit()
                self.ruleView.clearSelection()
    
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())