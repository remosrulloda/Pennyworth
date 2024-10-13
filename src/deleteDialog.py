from PySide6.QtWidgets import QDialog

from ui.ui_deleteRule import Ui_Dialog as delete_Dialog

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