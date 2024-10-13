import sys

from src.database import *
from src.move_file import move_file
from src.ruleItem import RuleItem
from src.addRuleDialog import AddRuleDialog
from src.ruleModel import RuleModel
from src.deleteDialog import DeleteDialog

from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QDialog, 
    QListWidgetItem
)
from PySide6.QtCore import Qt, QTimer

from ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = RuleModel()
        self.setWindowTitle("Pennyworth")

        # Create and load database
        create_table()
        self.load()

        # Connecting buttons
        self.addRuleBtn.pressed.connect(self.add)
        self.deleteRuleBtn.pressed.connect(self.delete)

        # Set up QTimer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.run_all_rules)
        self.timer.start(2000)

    def add(self):
        # Add a rule to the rule file rules list 
        dialog = AddRuleDialog()
        if dialog.exec():
            rule_data = dialog.getRuleData()
            if rule_data:
                new_id = self.insert(rule_data)
                rule_data['id'] = new_id
                
                item = QListWidgetItem(self.ruleView)

                rule_widget = RuleItem(rule_data)

                rule_widget.editRequested.connect(lambda data, item=item: self.edit(item, data))

                item.setData(Qt.UserRole, rule_data)
                item.setSizeHint(rule_widget.sizeHint())

                self.ruleView.addItem(item)
                self.ruleView.setItemWidget(item, rule_widget)

                self.model.addRule(rule_data)

    def edit(self, item, current_rule_data):
        dialog = AddRuleDialog()
        dialog.setRuleData(current_rule_data)

        if dialog.exec():
            updated_rule_data = dialog.getRuleData()

            # Make sure 'id' is preserved
            updated_rule_data['id'] = current_rule_data['id']

            print(f"Updating with dat: {updated_rule_data}")

            item.setData(Qt.UserRole, updated_rule_data)

            rule_widget = self.ruleView.itemWidget(item)
            rule_widget.ui.rule.setText(updated_rule_data['ruleName'])
            rule_widget.rule_data = updated_rule_data

            self.update(updated_rule_data, current_rule_data['id'])
        
    def delete(self):
        selected_indexes = self.ruleView.selectedItems()
        if not selected_indexes:
            return

        item = selected_indexes[0]
        rule_data = item.data(Qt.UserRole)

        print(f"\n\n{rule_data}")

        rule_id = rule_data['id']

        dialog = DeleteDialog(rule_data['ruleName'])
        if dialog.exec() == QDialog.Accepted:
            # Delete from the database
            self.deleteRulefromDB(rule_id)

            index = self.ruleView.row(item)
            self.model.beginRemoveColumns(self.model.index(index), index, index)
            del self.model.rules[index]
            self.model.endRemoveRows()

            self.ruleView.takeItem(self.ruleView.row(item))
            self.ruleView.clearSelection()

    def getSelectedRuleData(self):
        selected_items = self.ruleView.selectedItems()
        if not selected_items:
            return None
        
        selected_item = selected_items[0]
        rule_data = selected_item.data(Qt.UserRole)
        return rule_data
    
    def load(self):
        try:
            with sqlite3.connect("rules.db") as conn:

                cursor = conn.cursor()
                cursor.execute("SELECT * FROM rules")
                rows = cursor.fetchall()  # Fetch all rows from the executed query
                
                print(f"Total rules fetched: {len(rows)}")  # Debugging output
                
                self.model.rules.clear()
                self.ruleView.clear() 

                for row in rows:
                    print(f"Processing row: {row}")  # Debugging output
                    
                    rule_data = {
                        'id': row[0],
                        'ruleName': row[1],
                        'sourceDir': row[2],
                        'destDir': row[3],
                        'fileAttribute': row[4],
                        'comparisonOperator': row[5],
                        'comparisonValue': row[6],
                        'actionToTake': row[7],
                    }

                    self.model.addRule(rule_data)

                    item = QListWidgetItem(self.ruleView)
                    rule_widget = RuleItem(rule_data)
                    item.setData(Qt.UserRole, rule_data)
                    item.setSizeHint(rule_widget.sizeHint())
                    self.ruleView.addItem(item)
                    self.ruleView.setItemWidget(item, rule_widget)
                    rule_widget.editRequested.connect(lambda data, item=item: self.edit(item, data))

        except sqlite3.Error as e:
            print(f"Error loading rules: {e}")


    def insert(self, rule_id):
        with sqlite3.connect("rules.db") as conn:
            cursor = conn.cursor()
            
            for rule in self.model.rules:
                cursor.execute(
                '''
                    INSERT INTO rules (
                        rule_name, 
                        source_dir, 
                        dest_dir, 
                        file_attribute, 
                        comparison_operator, 
                        comparison_value, 
                        action_to_take
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    rule['ruleName'], 
                    rule['sourceDir'], 
                    rule['destDir'], 
                    rule['fileAttribute'],
                    rule['comparisonOperator'], 
                    rule['comparisonValue'], 
                    rule['actionToTake'],
                )
            )
            new_id = cursor.lastrowid
            conn.commit()

            return new_id

    def update(self, updated_rule_data, rule_id):
        try:
            with sqlite3.connect("rules.db") as conn:
                cursor = conn.cursor()

                cursor.execute(
                    '''
                    UPDATE rules
                    SET rule_name = ?, source_dir = ?, dest_dir = ?, file_attribute = ?, 
                    comparison_operator = ?, comparison_value = ?, action_to_take = ?
                    WHERE id = ?
                    ''', (
                        updated_rule_data['ruleName'], 
                        updated_rule_data['sourceDir'], 
                        updated_rule_data['destDir'], 
                        updated_rule_data['fileAttribute'], 
                        updated_rule_data['comparisonOperator'], 
                        updated_rule_data['comparisonValue'], 
                        updated_rule_data['actionToTake'], 
                        rule_id
                    )
                )
                conn.commit()
                print(f"Updated rule with id {rule_id}")
        except sqlite3.Error as e:
            print(f"Error updating rule in database: {e}")
    
    def deleteRulefromDB(self, rule_id):
        try:
            with sqlite3.connect("rules.db") as conn:
                cursor = conn.cursor()
                cursor.execute(
                    '''
                    DELETE FROM rules WHERE id = ?
                    ''', (rule_id,)
                )
                conn.commit()
                print(f"Deleted rule with {rule_id}")
        except sqlite3.Error as e:
            print(f"Error deleting rule from database: {e}")

    def run_all_rules(self):
        for rule in self.model.rules:
            try:
                move_file(
                    rule['comparisonOperator'],
                    rule['comparisonValue'],
                    rule['sourceDir'],
                    rule['destDir']
                )
                print(f"Applied rule: {rule['ruleName']}")
            except Exception as e:
                print(f"Error applying rule {rule['ruleName']}: {e}")

    def closeEvent(self, event):
        self.timer.stop()
        event.accept()
    
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())