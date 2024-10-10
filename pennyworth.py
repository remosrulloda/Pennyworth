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

    def addSourceDir(self):
        sourceName = QFileDialog.getExistingDirectory()
        if sourceName:
            self.sourceDir = sourceName
            self.customChangeEvent(sourceName)
            self.ui.folderSourceLabel.setText(sourceName)
            print(self.sourceDir)

    def addDestDir(self):
        destName = QFileDialog.getExistingDirectory()
        if destName:
            self.destDir = destName
            self.customChangeEvent(destName)
            self.ui.destFolderLabel.setText(destName)
            print(self.destDir)

    def customChangeEvent(self, fileName):
        print(f"Directory changed to {fileName}")

    
    def addRule(self):
        self.ruleName = self.ui.ruleNameEdit.text()
        self.fileAttribute = self.ui.ruleComboBox.currentText()
        self.comparisonOperator = self.ui.verbComboBox.currentText()
        self.comparisonValue = self.ui.lineEdit.text()
        self.actionToTake = self.ui.actionComboBox.currentText()

        # Accept and return the rule
        self.accept()
    
    def getRuleName(self):
        return f"{self.ruleName}"


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
            rule_text = dialog.getRuleName()
            if rule_text:
                self.model.addRule(("active", rule_text))

    
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())