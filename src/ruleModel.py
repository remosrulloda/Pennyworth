from PySide6.QtCore import Qt, QAbstractListModel, QModelIndex

class RuleModel(QAbstractListModel):
    def __init__(self, rules=None):
        super().__init__()
        self.rules = rules or []
    
    def data(self, index, role):
        if role == Qt.DisplayRole or role == Qt.DecorationRole:
            rule_data = self.rules[index.row()]
            return rule_data['ruleName']
        
    def rowCount(self, index):
        return len(self.rules)
            
    def addRule(self, rule_data):
        # self.beginInsertRows(self.index(len(self.rules)), len(self.rules), len(self.rules))
        self.beginInsertRows(QModelIndex(), len(self.rules), len(self.rules))
        self.rules.append(rule_data)
        self.endInsertRows()