# src/components/theme_manager.py

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QFile, QTextStream

class ThemeManager:
    def __init__(self, app: QApplication):
        self.app = app

    def apply_theme(self, theme: str):
        """Apply the chosen theme to the application."""
        theme_file = QFile(f"src/assets/themes/{theme}.qss")
        if theme_file.open(QFile.OpenModeFlag.ReadOnly):
            stream = QTextStream(theme_file)
            self.app.setStyleSheet(stream.readAll())
        theme_file.close()
