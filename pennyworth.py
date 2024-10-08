import sys
from PySide6.QtCore import Qt, QAbstractListModel
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QSystemTrayIcon, 
    QMenu, 
    QFileDialog
)
from PySide6.QtGui import QIcon, QAction
from MainWindow import Ui_MainWindow
from file_mover import move_files

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

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.model = FolderModel()
        self.folderView.setModel(self.model)

        #Connect the buttons
        self.addFolderBtn.pressed.connect(self.addFolder)
        # self.addRule.pressed.connect(self.addRule)
    
    def initUI(self):
        self.setWindowTitle("Pennyworth")
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowIcon(QIcon("icon.png"))  

    def addFolder(self):
        """
        Adds a folder to the folderView, 
        getting the folder text from the QDialog
        """        
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")

        if folder: 
            self.model.folders.append(folder)
            self.model.layoutChanged.emit()
    
    def moveFiles(self):
        if self.folder:
            move_files()
    




        

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


# class TrayApp(QApplication):
#     def __init__(self, args):
#         super().__init__(args)
#         self.main_window = MainWindow()

#         # Create the system tray icon
#         self.tray_icon = QSystemTrayIcon(QIcon("icon.png"), self) 
#         self.tray_icon.setToolTip("Pennyworth")

#         # Create a context menu for the tray icon
#         tray_menu = QMenu()
#         open_action = QAction("Open", self)
#         open_action.triggered.connect(self.show_window)
#         exit_action = QAction("Exit", self)
#         exit_action.triggered.connect(self.exit_app)
#         settings_action = QAction("Settings", self)
#         settings_action.triggered.connect(self.exit_app)

#         tray_menu.addAction(open_action)
#         tray_menu.addAction(settings_action)
#         tray_menu.addAction(exit_action)

#         self.tray_icon.setContextMenu(tray_menu)
#         self.tray_icon.activated.connect(self.on_tray_icon_clicked)
#         self.tray_icon.show()

#     def show_window(self):
#         self.main_window.show()

#     def exit_app(self):
#         self.quit()

#     def on_tray_icon_clicked(self, reason):
#         # Handle click events for the tray icon
#         if reason == QSystemTrayIcon.Trigger: 
#             if not self.main_window.isVisible():
#                 self.main_window.show()
#             else:
#                 self.main_window.hide()
