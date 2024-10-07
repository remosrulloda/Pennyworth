import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pennyworth")
        self.setGeometry(100, 100, 300, 200)
        self.setWindowIcon(QIcon("icon.png"))  

class TrayApp(QApplication):
    def __init__(self, args):
        super().__init__(args)
        self.main_window = MainWindow()

        # Create the system tray icon
        self.tray_icon = QSystemTrayIcon(QIcon("icon.png"), self) 
        self.tray_icon.setToolTip("Pennyworth")

        # Create a context menu for the tray icon
        tray_menu = QMenu()
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.show_window)
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.exit_app)
        settings_action = QAction("Settings", self)
        settings_action.triggered.connect(self.exit_app)

        tray_menu.addAction(open_action)
        tray_menu.addAction(settings_action)
        tray_menu.addAction(exit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.activated.connect(self.on_tray_icon_clicked)
        self.tray_icon.show()

    def show_window(self):
        self.main_window.show()

    def exit_app(self):
        self.quit()

    def on_tray_icon_clicked(self, reason):
        # Handle click events for the tray icon
        if reason == QSystemTrayIcon.Trigger: 
            if not self.main_window.isVisible():
                self.main_window.show()
            else:
                self.main_window.hide()

if __name__ == "__main__":
    app = TrayApp([])
    sys.exit(app.exec())
