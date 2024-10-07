import sys


from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Pennyworth')

        button = QPushButton("Press Me!")

        self.setFixedSize(QSize(900, 500))

        self.setCentralWidget(button)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()

# activate via source .venv/bin/activate