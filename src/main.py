# src/main.py

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from components.editor import Editor
from components.menu import MenuBar
from components.status_bar import StatusBar

class PixelPad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pixel Pad")
        self.setGeometry(100, 100, 800, 600)

        # Initialize components
        self.editor = Editor(self)
        self.menu_bar = MenuBar(self)
        self.status_bar = StatusBar(self)

        # Set up the layout
        self.setCentralWidget(self.editor)
        self.setMenuBar(self.menu_bar)
        self.setStatusBar(self.status_bar)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PixelPad()
    window.show()
    sys.exit(app.exec())
