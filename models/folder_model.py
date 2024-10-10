from PySide6.QtCore import Qt, QAbstractListModel

class FolderModel(QAbstractListModel):
    def __init__(self, folders=None):
        super().__init__()
        self.folders = folders or []
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            text = self.folders[index.row()]
            return text
        
    def rowCount(self, index):
        return len(self.folders)