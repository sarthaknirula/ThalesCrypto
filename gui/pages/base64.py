from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class Base64Page(QWidget):
    """Placeholder page for the Base64 module."""

    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("placeholderPage")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(48, 48, 48, 48)
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("Base64")
        title.setObjectName("placeholderTitle")
        title.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)
