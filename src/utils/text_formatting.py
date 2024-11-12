# src/utils/text_formatting.py

def to_uppercase(text: str) -> str:
    """Convert the given text to uppercase."""
    return text.upper()

def to_lowercase(text: str) -> str:
    """Convert the given text to lowercase."""
    return text.lower()

def bold_text(text: str) -> str:
    """Return the text in bold (as HTML)."""
    return f"<b>{text}</b>"
