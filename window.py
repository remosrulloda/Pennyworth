import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QLabel
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Pennyworth')

        widget = QLabel("File Rules")
        font = widget.font()
        font.setPointSize(24)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.setCentralWidget(widget)



app = QApplication([])

window = MainWindow()
window.resize(1000, 600)
window.show()

app.exec()

# activate via source .venv/bin/activate