# src/components/menu.py

from PyQt6.QtWidgets import QMenuBar, QMenu, QAction

class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # File menu
        file_menu = QMenu("File", self)
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        exit_action = QAction("Exit", self)

        # Add actions to the menu
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(exit_action)

        # Add the File menu to the menu bar
        self.addMenu(file_menu)
