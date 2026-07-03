from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QButtonGroup,
    QFileDialog,
    QFormLayout,
    QFrame,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QRadioButton,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from crypto.rsa import RSAService


class RSAPage(QWidget):
    """RSA workspace for key generation and file operations."""

    MILESTONE_MESSAGE = "Functionality will be implemented in Milestone 3."

    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("rsaPage")
        self.rsa_service = RSAService()
        self._build_layout()
        self._apply_styles()

    def _build_layout(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        scroll_area = QScrollArea()
        scroll_area.setObjectName("rsaScrollArea")
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.NoFrame)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        content = QWidget()
        content.setObjectName("rsaContent")
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(48, 42, 48, 42)
        content_layout.setSpacing(24)
        content_layout.setAlignment(Qt.AlignTop)

        title = QLabel("RSA Workspace")
        title.setObjectName("rsaTitle")

        subtitle = QLabel("Generate RSA key pairs and prepare file encryption workflows.")
        subtitle.setObjectName("rsaSubtitle")

        content_layout.addWidget(title)
        content_layout.addWidget(subtitle)
        content_layout.addWidget(self._create_key_generation_group())
        content_layout.addWidget(self._create_encryption_group())
        content_layout.addWidget(self._create_decryption_group())
        content_layout.addStretch()

        scroll_area.setWidget(content)
        layout.addWidget(scroll_area)

    def _create_key_generation_group(self) -> QGroupBox:
        group = QGroupBox("RSA Key Generation")
        group.setMinimumHeight(188)
        group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout = QVBoxLayout(group)
        layout.setContentsMargins(22, 28, 22, 22)
        layout.setSpacing(18)

        key_size_label = QLabel("Key Size")
        key_size_label.setObjectName("fieldLabel")

        key_size_layout = QHBoxLayout()
        key_size_layout.setContentsMargins(0, 0, 0, 0)
        key_size_layout.setSpacing(34)

        self.key_size_group = QButtonGroup(self)
        for size in ("2048", "3072", "4096"):
            button = QRadioButton(size)
            button.setCursor(Qt.PointingHandCursor)
            button.setChecked(size == "4096")
            button.setFixedWidth(96)
            button.setMinimumHeight(28)
            self.key_size_group.addButton(button)
            key_size_layout.addWidget(button)
        key_size_layout.addStretch()

        self.save_location_input = QLineEdit()
        self.save_location_input.setPlaceholderText("Select folder for generated keys")

        browse_save_button = self._create_browse_button()
        browse_save_button.clicked.connect(
            lambda: self._browse_folder(self.save_location_input)
        )

        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignLeft)
        form.setFormAlignment(Qt.AlignTop)
        form.setHorizontalSpacing(18)
        form.setVerticalSpacing(16)
        form.setRowWrapPolicy(QFormLayout.WrapLongRows)
        form.addRow(key_size_label, key_size_layout)
        form.addRow(
            "Save Location",
            self._create_path_row(self.save_location_input, browse_save_button),
        )

        generate_button = QPushButton("Generate Keys")
        generate_button.setObjectName("primaryButton")
        generate_button.setCursor(Qt.PointingHandCursor)
        generate_button.clicked.connect(self._generate_keys)

        button_row = QHBoxLayout()
        button_row.addStretch()
        button_row.addWidget(generate_button)

        layout.addLayout(form)
        layout.addLayout(button_row)
        return group

    def _create_encryption_group(self) -> QGroupBox:
        group = QGroupBox("File Encryption")
        group.setMinimumHeight(212)
        group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout = QVBoxLayout(group)
        layout.setContentsMargins(22, 28, 22, 22)
        layout.setSpacing(18)

        self.public_key_input = QLineEdit()
        self.public_key_input.setPlaceholderText("Select RSA public key")
        public_key_browse = self._create_browse_button()
        public_key_browse.clicked.connect(lambda: self._browse_file(self.public_key_input))

        self.input_file_input = QLineEdit()
        self.input_file_input.setPlaceholderText("Select file to encrypt")
        input_file_browse = self._create_browse_button()
        input_file_browse.clicked.connect(lambda: self._browse_file(self.input_file_input))

        self.encrypt_output_folder_input = QLineEdit()
        self.encrypt_output_folder_input.setPlaceholderText("Select encrypted output folder")
        encrypt_output_browse = self._create_browse_button()
        encrypt_output_browse.clicked.connect(
            lambda: self._browse_folder(self.encrypt_output_folder_input)
        )

        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignLeft)
        form.setFormAlignment(Qt.AlignTop)
        form.setHorizontalSpacing(18)
        form.setVerticalSpacing(16)
        form.setRowWrapPolicy(QFormLayout.WrapLongRows)
        form.addRow(
            "Public Key",
            self._create_path_row(self.public_key_input, public_key_browse),
        )
        form.addRow(
            "Input File",
            self._create_path_row(self.input_file_input, input_file_browse),
        )
        form.addRow(
            "Output Folder",
            self._create_path_row(self.encrypt_output_folder_input, encrypt_output_browse),
        )

        encrypt_button = QPushButton("Encrypt")
        encrypt_button.setObjectName("primaryButton")
        encrypt_button.setCursor(Qt.PointingHandCursor)
        encrypt_button.clicked.connect(self._show_milestone_message)

        button_row = QHBoxLayout()
        button_row.addStretch()
        button_row.addWidget(encrypt_button)

        layout.addLayout(form)
        layout.addLayout(button_row)
        return group

    def _create_decryption_group(self) -> QGroupBox:
        group = QGroupBox("File Decryption")
        group.setMinimumHeight(212)
        group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout = QVBoxLayout(group)
        layout.setContentsMargins(22, 28, 22, 22)
        layout.setSpacing(18)

        self.private_key_input = QLineEdit()
        self.private_key_input.setPlaceholderText("Select RSA private key")
        private_key_browse = self._create_browse_button()
        private_key_browse.clicked.connect(lambda: self._browse_file(self.private_key_input))

        self.encrypted_file_input = QLineEdit()
        self.encrypted_file_input.setPlaceholderText("Select encrypted file")
        encrypted_file_browse = self._create_browse_button()
        encrypted_file_browse.clicked.connect(
            lambda: self._browse_file(self.encrypted_file_input)
        )

        self.decrypt_output_folder_input = QLineEdit()
        self.decrypt_output_folder_input.setPlaceholderText("Select decrypted output folder")
        decrypt_output_browse = self._create_browse_button()
        decrypt_output_browse.clicked.connect(
            lambda: self._browse_folder(self.decrypt_output_folder_input)
        )

        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignLeft)
        form.setFormAlignment(Qt.AlignTop)
        form.setHorizontalSpacing(18)
        form.setVerticalSpacing(16)
        form.setRowWrapPolicy(QFormLayout.WrapLongRows)
        form.addRow(
            "Private Key",
            self._create_path_row(self.private_key_input, private_key_browse),
        )
        form.addRow(
            "Encrypted File",
            self._create_path_row(self.encrypted_file_input, encrypted_file_browse),
        )
        form.addRow(
            "Output Folder",
            self._create_path_row(self.decrypt_output_folder_input, decrypt_output_browse),
        )

        decrypt_button = QPushButton("Decrypt")
        decrypt_button.setObjectName("primaryButton")
        decrypt_button.setCursor(Qt.PointingHandCursor)
        decrypt_button.clicked.connect(self._show_milestone_message)

        button_row = QHBoxLayout()
        button_row.addStretch()
        button_row.addWidget(decrypt_button)

        layout.addLayout(form)
        layout.addLayout(button_row)
        return group

    def _create_path_row(self, line_edit: QLineEdit, browse_button: QPushButton) -> QWidget:
        row = QWidget()
        layout = QHBoxLayout(row)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)
        layout.addWidget(line_edit, stretch=1)
        layout.addWidget(browse_button)
        return row

    def _create_browse_button(self) -> QPushButton:
        button = QPushButton("Browse")
        button.setObjectName("secondaryButton")
        button.setCursor(Qt.PointingHandCursor)
        return button

    def _browse_file(self, target: QLineEdit) -> None:
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
        if file_path:
            target.setText(file_path)

    def _browse_folder(self, target: QLineEdit) -> None:
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            target.setText(folder_path)

    def _generate_keys(self) -> None:
        selected_button = self.key_size_group.checkedButton()
        key_size = int(selected_button.text()) if selected_button else 4096

        if key_size != 4096:
            QMessageBox.information(
                self,
                "Future Milestone",
                "This key size will be implemented in a future milestone.",
            )
            return

        save_location = self.save_location_input.text().strip()
        save_directory = Path(save_location) if save_location else None

        try:
            public_key_path, private_key_path = self.rsa_service.generate_key_pair(
                key_size,
                save_directory,
            )
            QMessageBox.information(
                self,
                "RSA Keys Generated",
                "RSA 4096-bit key pair generated successfully.\n\n"
                f"Public Key:\n{public_key_path.resolve()}\n\n"
                f"Private Key:\n{private_key_path.resolve()}",
            )
        except Exception as exc:
            QMessageBox.critical(self, "RSA Key Generation Failed", str(exc))

    def _show_milestone_message(self) -> None:
        QMessageBox.information(self, "Milestone 3", self.MILESTONE_MESSAGE)

    def _apply_styles(self) -> None:
        self.setStyleSheet(
            """
            #rsaPage {
                background-color: #121212;
                color: #ffffff;
            }

            #rsaScrollArea,
            #rsaScrollArea > QWidget > QWidget,
            #rsaContent {
                background-color: #121212;
            }

            #rsaTitle {
                color: #ffffff;
                font-size: 32px;
                font-weight: 800;
            }

            #rsaSubtitle {
                color: #B0B0B0;
                font-size: 15px;
            }

            QGroupBox {
                background-color: #1F1F1F;
                border: 1px solid #303030;
                border-radius: 8px;
                color: #ffffff;
                font-size: 17px;
                font-weight: 700;
                margin-top: 14px;
            }

            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                left: 16px;
                padding: 0 8px;
            }

            QLabel,
            QRadioButton {
                color: #D8D8D8;
                font-size: 14px;
                font-weight: 500;
            }

            #fieldLabel {
                color: #D8D8D8;
            }

            QRadioButton {
                spacing: 9px;
                padding-right: 10px;
            }

            QLineEdit {
                background-color: #151515;
                border: 1px solid #3A3A3A;
                border-radius: 6px;
                color: #ffffff;
                font-size: 14px;
                min-height: 38px;
                padding: 0 12px;
            }

            QLineEdit:focus {
                border: 1px solid #39C2D7;
            }

            QLineEdit::placeholder {
                color: #7F7F7F;
            }

            QRadioButton::indicator {
                height: 16px;
                width: 16px;
            }

            QRadioButton::indicator:unchecked {
                border: 2px solid #6A6A6A;
                border-radius: 8px;
                background-color: #151515;
            }

            QRadioButton::indicator:checked {
                border: 2px solid #39C2D7;
                border-radius: 8px;
                background-color: #39C2D7;
            }

            #primaryButton,
            #secondaryButton {
                border: none;
                border-radius: 6px;
                color: #ffffff;
                font-size: 14px;
                font-weight: 700;
                min-height: 38px;
                padding: 0 18px;
            }

            #primaryButton {
                background-color: #005BBB;
                min-width: 138px;
            }

            #primaryButton:hover {
                background-color: #1976D2;
            }

            #secondaryButton {
                background-color: #2D2D2D;
                min-width: 92px;
            }

            #secondaryButton:hover {
                background-color: #3A3A3A;
            }
            """
        )
