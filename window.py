import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QLabel,
    QFileDialog,
    QPushButton,
    QSystemTrayIcon
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pennyworth')
        self.setGeometry(100, 100, 300, 200)

        widget = QLabel("File Rules")
        font = widget.font()
        font.setPointSize(24)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.setCentralWidget(widget)

        sourceBtn = QPushButton("Select Source Folder")
        sourceBtn.clicked.connect(self.get_directory)

        self.setCentralWidget(sourceBtn)

    def get_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Source Folder")
        print("Selected directory:" , directory)
    

app = QApplication([])

window = MainWindow()
window.resize(1000, 600)
window.show()

app.exec()

# activate via source .venv/bin/activate