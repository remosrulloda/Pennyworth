from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from models.folder_model import FolderModel
from ui.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

        self.model = FolderModel()
        self.folderViewer.setModel(self.model)

        # Connect the buttons
        self.addFolderBtn.pressed.connect(self.addFolder)
        self.addRuleBtn.pressed.connect(self.addRule)
    
    def initUI(self):
        self.setWindowTitle("Pennyworth")
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowIcon(QIcon("/img/icon.png"))  

    def addFolder(self):
        """
        Adds a folder to the folderView, 
        getting the folder text from the QDialog
        """        
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder: 
            self.model.folders.append(folder)
            self.model.layoutChanged.emit()
    
    def addRule(self):
        """
        Adds a rule to the ruleViewer
        """
        indexes = self.folderViewer.selectedIndexes()

        if indexes:
            selectedFolderIndex = indexes[0]    
            selectedFolder = self.folderViewer.model().data(selectedFolderIndex, role=Qt.DisplayRole)
            


            
            