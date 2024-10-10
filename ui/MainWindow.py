from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from ui.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.ruleViewer.setModel(self.model)
    
    def initUI(self):
        self.setWindowTitle("Pennyworth")
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowIcon(QIcon("/img/icon.png"))  
            


            
            