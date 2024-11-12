# src/components/editor.py

from PyQt6.QtWidgets import QTextEdit

class Editor(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPlaceholderText("Start typing here...")
        self.setAcceptRichText(False)  # Plain text for simplicity
