from pathlib import Path

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from gui.pages.aes import AESPage
from gui.pages.base64 import Base64Page
from gui.pages.home import HomePage
from gui.pages.merge import FileMergePage
from gui.pages.rsa import RSAPage
from gui.pages.settings import SettingsPage


PROJECT_ROOT = Path(__file__).resolve().parents[1]
APP_ICON_PATH = PROJECT_ROOT / "assets" / "icons" / "thales-sa-ho.png"


class MainWindow(QMainWindow):
    """Main application shell for Thales Crypto."""

    WINDOW_TITLE = "Thales Crypto"
    INITIAL_WIDTH = 1400
    INITIAL_HEIGHT = 850
    SIDEBAR_WIDTH = 220

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(self.WINDOW_TITLE)
        self.resize(self.INITIAL_WIDTH, self.INITIAL_HEIGHT)

        self._pages = QStackedWidget()
        self._navigation_buttons: dict[str, QPushButton] = {}

        self._configure_window()
        self._build_layout()
        self._register_pages()
        self._apply_styles()

    def _configure_window(self) -> None:
        self.setMinimumSize(1000, 650)
        if APP_ICON_PATH.exists():
            self.setWindowIcon(QIcon(str(APP_ICON_PATH)))

    def _build_layout(self) -> None:
        root = QWidget()
        root_layout = QHBoxLayout(root)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        root_layout.addWidget(self._create_sidebar())
        root_layout.addWidget(self._create_content_area(), stretch=1)

        self.setCentralWidget(root)

    def _create_sidebar(self) -> QFrame:
        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(self.SIDEBAR_WIDTH)

        layout = QVBoxLayout(sidebar)
        layout.setContentsMargins(18, 24, 18, 24)
        layout.setSpacing(10)

        brand_row = QHBoxLayout()
        brand_row.setContentsMargins(0, 0, 0, 0)
        brand_row.setSpacing(10)

        icon = QLabel()
        icon.setObjectName("sidebarIcon")
        icon.setFixedSize(34, 34)
        if APP_ICON_PATH.exists():
            pixmap = QPixmap(str(APP_ICON_PATH))
            if not pixmap.isNull():
                icon.setPixmap(
                    pixmap.scaled(34, 34, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                )
        brand_row.addWidget(icon)

        brand = QLabel("Thales Crypto")
        brand.setObjectName("sidebarBrand")
        brand.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        brand_row.addWidget(brand, stretch=1)

        layout.addLayout(brand_row)
        layout.addSpacing(22)

        for label in ("Home", "RSA", "AES", "Base64", "File Merge", "Settings"):
            button = self._create_navigation_button(label)
            layout.addWidget(button)
            self._navigation_buttons[label] = button

        layout.addStretch()
        return sidebar

    def _create_navigation_button(self, label: str) -> QPushButton:
        button = QPushButton(label)
        button.setObjectName("navigationButton")
        button.setCursor(Qt.PointingHandCursor)
        button.setMinimumHeight(46)
        button.setIconSize(QSize(18, 18))
        return button

    def _create_content_area(self) -> QFrame:
        content = QFrame()
        content.setObjectName("contentArea")

        layout = QVBoxLayout(content)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self._pages)

        return content

    def _register_pages(self) -> None:
        page_factories = (
            ("Home", HomePage),
            ("RSA", RSAPage),
            ("AES", AESPage),
            ("Base64", Base64Page),
            ("File Merge", FileMergePage),
            ("Settings", SettingsPage),
        )

        for index, (label, page_factory) in enumerate(page_factories):
            self._pages.addWidget(page_factory())
            button = self._navigation_buttons.get(label)
            if button is not None:
                button.clicked.connect(lambda checked=False, i=index: self._show_page(i))

        self._pages.setCurrentIndex(0)
        self._set_active_button(0)

    def _show_page(self, index: int) -> None:
        self._pages.setCurrentIndex(index)
        self._set_active_button(index)

    def _set_active_button(self, active_index: int) -> None:
        for index, button in enumerate(self._navigation_buttons.values()):
            button.setProperty("active", index == active_index)
            button.style().unpolish(button)
            button.style().polish(button)

    def _apply_styles(self) -> None:
        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #121212;
                color: #ffffff;
            }

            #sidebar {
                background-color: #1B1B1B;
                border-right: 1px solid #2d2d2d;
            }

            #sidebarIcon {
                background-color: transparent;
            }

            #sidebarBrand {
                color: #ffffff;
                font-size: 18px;
                font-weight: 700;
            }

            #navigationButton {
                background-color: transparent;
                border: none;
                border-radius: 8px;
                color: #B0B0B0;
                font-size: 15px;
                font-weight: 600;
                padding: 11px 14px;
                text-align: left;
            }

            #navigationButton:hover {
                background-color: #1976D2;
                color: #ffffff;
            }

            #navigationButton[active="true"] {
                background-color: #005BBB;
                color: #ffffff;
            }

            #contentArea {
                background-color: #121212;
            }

            QStackedWidget {
                background-color: #121212;
            }

            #placeholderPage {
                background-color: #121212;
            }

            #placeholderTitle {
                color: #ffffff;
                font-size: 34px;
                font-weight: 700;
            }

            #placeholderSubtitle {
                color: #B0B0B0;
                font-size: 15px;
            }
            """
        )
