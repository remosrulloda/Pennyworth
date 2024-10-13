import uuid

from PySide6.QtWidgets import QFileDialog, QDialog, QMessageBox

from ui.ui_addRule import Ui_Dialog

class AddRuleDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Add Rule")

        # Rule members
        self.uuid = str(uuid.uuid4())
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

    def addSourceDir(self):
        sourceName = QFileDialog.getExistingDirectory()
        if sourceName:
            self.sourceDir = sourceName
            self.customChangeEvent("Source", sourceName)
            self.ui.folderSourceLabel.setText(sourceName)
            self.onInputChange('source')

    def addDestDir(self):
        destName = QFileDialog.getExistingDirectory()
        if destName:
            self.destDir = destName
            self.customChangeEvent("Destination", destName)
            self.ui.destFolderLabel.setText(destName)
            self.onInputChange('dest')

    def customChangeEvent(self, dir, fileName):
        print(f"{dir} changed to {fileName}")

    def addRule(self):
        self.ruleName = self.ui.ruleNameEdit.text().strip()
        self.fileAttribute = self.ui.ruleComboBox.currentText().strip()
        self.comparisonOperator = self.ui.verbComboBox.currentText().strip()
        self.comparisonValue = self.ui.lineEdit.text().strip()
        self.actionToTake = self.ui.actionComboBox.currentText().strip()

        # Validate Inputs
        validation_map = {
            "Name": self.ruleName,
            "Source Directory": self.sourceDir,
            "Destination Directory": self.destDir,
            "File Attribute": self.fileAttribute,
            "Comparison Operator": self.comparisonOperator,
            "Comparison Value": self.comparisonValue,
            "Action": self.actionToTake,
        }

        missing_fields = []

        for field_name, value in validation_map.items():
            if not value:
                missing_fields.append(field_name)

        if missing_fields:
            self.highlightMissingFields(missing_fields)
            return
    
        self.accept()

    def setRuleData(self, rule_data):
        self.uuid = rule_data['uuid']
        self.ruleName = rule_data['ruleName']
        self.sourceDir = rule_data['sourceDir']
        self.destDir = rule_data['destDir']
        self.fileAttribute = rule_data['fileAttribute']
        self.comparisonOperator = rule_data['comparisonOperator']
        self.comparisonValue = rule_data['comparisonValue']
        self.actionToTake = rule_data['actionToTake']
    
        self.ui.ruleNameEdit.setText(self.ruleName)
        self.ui.folderSourceLabel.setText(self.sourceDir)
        self.ui.destFolderLabel.setText(self.destDir)
        self.ui.ruleComboBox.setCurrentText(self.fileAttribute)
        self.ui.verbComboBox.setCurrentText(self.comparisonOperator)
        self.ui.lineEdit.setText(self.comparisonValue)
        self.ui.actionComboBox.setCurrentText(self.actionToTake)
    
    def getRuleData(self):
        return {
            'uuid': self.uuid,
            'ruleName': self.ruleName,
            'sourceDir': self.sourceDir,
            'destDir': self.destDir, 
            'fileAttribute': self.fileAttribute,
            'comparisonOperator': self.comparisonOperator,
            'comparisonValue': self.comparisonValue,
            'actionToTake': self.actionToTake
        }

    def getRuleName(self):
        return f"{self.ruleName}"

    def showErrorMessage(self, message):
        QMessageBox.warning(self, "Input Error", message)
    
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

    def highlightMissingFields(self, missing_fields: dict):
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
