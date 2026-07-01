from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class AESPage(QWidget):
    """Placeholder page for the AES module."""

    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("placeholderPage")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(48, 48, 48, 48)
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("AES")
        title.setObjectName("placeholderTitle")
        title.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)
