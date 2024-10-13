from ui.ui_Rule import Ui_Form 
from PySide6.QtWidgets import QWidget

from PySide6.QtCore import Signal


class RuleItem(QWidget, Ui_Form):
    editRequested = Signal(dict)

    def __init__(self, rule_data, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.rule_data = rule_data

        self.ui.rule.setText(self.rule_data['ruleName'])
        self.ui.rule.setChecked(True)
        self.ui.editRuleBtn.pressed.connect(self.requestEdit)

    def requestEdit(self):
        self.editRequested.emit(self.rule_data)