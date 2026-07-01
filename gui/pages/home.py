from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget


PROJECT_ROOT = Path(__file__).resolve().parents[2]
LOGO_PATH = PROJECT_ROOT / "assets" / "logo" / "logo.png"


class HomePage(QWidget):
    """Landing page shown when the application starts."""

    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("homePage")
        self._build_layout()
        self._apply_styles()

    def _build_layout(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(72, 72, 72, 72)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignCenter)

        content = QFrame()
        content.setObjectName("homeCard")
        content.setMaximumWidth(760)

        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(56, 52, 56, 52)
        content_layout.setSpacing(18)
        content_layout.setAlignment(Qt.AlignCenter)

        logo = QLabel()
        logo.setObjectName("homeLogo")
        logo.setAlignment(Qt.AlignCenter)
        logo.setFixedSize(132, 132)
        if LOGO_PATH.exists():
            pixmap = QPixmap(str(LOGO_PATH))
            if not pixmap.isNull():
                logo.setPixmap(
                    pixmap.scaled(132, 132, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                )

        title = QLabel("THALES CRYPTO")
        title.setObjectName("homeTitle")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("AI Powered Cryptographic Assistant")
        subtitle.setObjectName("homeSubtitle")
        subtitle.setAlignment(Qt.AlignCenter)

        welcome = QLabel(
            "Welcome to a focused workspace for cryptographic modules, secure file "
            "utilities, and guided operations."
        )
        welcome.setObjectName("homeWelcome")
        welcome.setAlignment(Qt.AlignCenter)
        welcome.setWordWrap(True)
        welcome.setMaximumWidth(620)

        content_layout.addWidget(logo, alignment=Qt.AlignCenter)
        content_layout.addSpacing(8)
        content_layout.addWidget(title)
        content_layout.addWidget(subtitle)
        content_layout.addSpacing(8)
        content_layout.addWidget(welcome)

        layout.addWidget(content)

    def _apply_styles(self) -> None:
        self.setStyleSheet(
            """
            #homePage {
                background-color: #121212;
            }

            #homeCard {
                background-color: #232323;
                border: 1px solid #303030;
                border-radius: 8px;
            }

            #homeLogo {
                background-color: transparent;
            }

            #homeTitle {
                color: #ffffff;
                font-size: 44px;
                font-weight: 800;
            }

            #homeSubtitle {
                color: #39C2D7;
                font-size: 22px;
                font-weight: 600;
            }

            #homeWelcome {
                color: #B0B0B0;
                font-size: 17px;
            }
            """
        )
