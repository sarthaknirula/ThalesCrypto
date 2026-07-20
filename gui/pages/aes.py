from crypto.aes import AESService
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout , QWidget , QLabel , QComboBox , QLineEdit , QPushButton , QFormLayout , QHBoxLayout , QFileDialog

class AESPage(QWidget) :
    def __init__(self) :
        super().__init__()
        self.service = AESService()

        self._create_header_widgets()
        self._create_key_generation_widgets()
        self._create_encryption_widgets()
        self._create_decryption_widgets()

        self._create_layout()
        self._connect_signals()

    def _create_header_widgets(self) -> None :
        
        self.header_label = QLabel('AES Workspace')
        self.subtitle_label = QLabel(
            "Generate AES Keys • Encrypt Files • Decrypt Files"
        )
        
    def _create_key_generation_widgets(self) -> None :

        self.key_generation_label = QLabel('AES Key Generation')
        self.key_size_label = QLabel('Select Key Size')
        self.key_size_combo = QComboBox()
        self.key_size_combo.addItems(['AES-128' , 'AES-192' , 'AES-256'])
        self.save_folder_label = QLabel('Save Folder')
        self.save_folder_line_edit = QLineEdit()
        self.save_folder_browse_button = QPushButton('Browse')
        self.generate_key_button = QPushButton('Generate Key')

    def _create_key_generation_layout(self) -> QVBoxLayout:

        key_generation_layout = QVBoxLayout()

        # Section Title
        key_generation_layout.addWidget(self.key_generation_label)

        # Form Layout
        form_layout = QFormLayout()

        form_layout.addRow(
            self.key_size_label,
            self.key_size_combo
        )

        save_folder_layout = QHBoxLayout()
        save_folder_layout.addWidget(self.save_folder_line_edit)
        save_folder_layout.addWidget(self.save_folder_browse_button)

        form_layout.addRow(
            self.save_folder_label,
            save_folder_layout
        )

        key_generation_layout.addLayout(form_layout)

        # Button Layout
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.generate_key_button)

        key_generation_layout.addLayout(button_layout)

        return key_generation_layout
    
    def _create_layout(self) -> None:

        main_layout = QVBoxLayout()

        header_layout = QVBoxLayout()
        header_layout.addWidget(self.header_label)
        header_layout.addWidget(self.subtitle_label)

        main_layout.addLayout(header_layout)

        main_layout.addLayout(
            self._create_key_generation_layout()
        )   

        # Later
        main_layout.addLayout(self._create_encryption_layout())
        main_layout.addLayout(self._create_decryption_layout())

        self.setLayout(main_layout)

    def _create_encryption_widgets(self) :

        self.encryption_label = QLabel('File Encryption')
        self.enc_key_file_label = QLabel('Key File')
        self.enc_key_file_line_edit = QLineEdit()
        self.enc_key_file_browse_button = QPushButton('Browse')
        self.enc_input_file_label = QLabel('Input File')
        self.enc_input_file_line_edit = QLineEdit()
        self.enc_input_file_browse_button = QPushButton('Browse')
        self.enc_output_folder_label = QLabel('Output Folder')
        self.enc_output_folder_line_edit = QLineEdit()
        self.enc_output_folder_browse_button = QPushButton('Browse')
        self.encrypt_file_button = QPushButton('Encrypt')

    def _create_decryption_widgets(self) :
        
        self.decryption_label = QLabel('File Decryption')
        self.dec_key_file_label = QLabel('Key File')
        self.dec_key_file_line_edit = QLineEdit()
        self.dec_key_file_browse_button = QPushButton('Browse')
        self.dec_input_file_label = QLabel('Input File')
        self.dec_input_file_line_edit = QLineEdit()
        self.dec_input_file_browse_button = QPushButton('Browse')
        self.dec_output_folder_label = QLabel('Output Folder')
        self.dec_output_folder_line_edit = QLineEdit()
        self.dec_output_folder_browse_button = QPushButton('Browse')
        self.decrypt_file_button = QPushButton('Decrypt')

    def _create_encryption_layout(self) -> QVBoxLayout :

        encryption_layout = QVBoxLayout()
        encryption_layout.addWidget(self.encryption_label)

        form_layout = QFormLayout()

        key_file_layout = QHBoxLayout()
        key_file_layout.addWidget(self.enc_key_file_line_edit)
        key_file_layout.addWidget(self.enc_key_file_browse_button)

        form_layout.addRow(self.enc_key_file_label,key_file_layout)

        input_file_layout = QHBoxLayout()
        input_file_layout.addWidget(self.enc_input_file_line_edit)
        input_file_layout.addWidget(self.enc_input_file_browse_button)

        form_layout.addRow(self.enc_input_file_label,input_file_layout)

        output_folder_layout = QHBoxLayout()
        output_folder_layout.addWidget(self.enc_output_folder_line_edit)
        output_folder_layout.addWidget(self.enc_output_folder_browse_button)

        form_layout.addRow(self.enc_output_folder_label,output_folder_layout)

        encryption_layout.addLayout(form_layout)

        encrypt_button_layout = QHBoxLayout()
        encrypt_button_layout.addWidget(self.encrypt_file_button)

        encryption_layout.addLayout(encrypt_button_layout)

        return encryption_layout

    def _create_decryption_layout(self) -> QVBoxLayout :

        decryption_layout = QVBoxLayout()
        decryption_layout.addWidget(self.decryption_label)

        form_layout = QFormLayout()

        key_file_layout = QHBoxLayout()
        key_file_layout.addWidget(self.dec_key_file_line_edit)
        key_file_layout.addWidget(self.dec_key_file_browse_button)

        form_layout.addRow(self.dec_key_file_label,key_file_layout)

        input_file_layout = QHBoxLayout()
        input_file_layout.addWidget(self.dec_input_file_line_edit)
        input_file_layout.addWidget(self.dec_input_file_browse_button)

        form_layout.addRow(self.dec_input_file_label,input_file_layout)

        output_folder_layout = QHBoxLayout()
        output_folder_layout.addWidget(self.dec_output_folder_line_edit)
        output_folder_layout.addWidget(self.dec_output_folder_browse_button)

        form_layout.addRow(self.dec_output_folder_label,output_folder_layout)

        decryption_layout.addLayout(form_layout)

        decrypt_button_layout = QHBoxLayout()
        decrypt_button_layout.addWidget(self.decrypt_file_button)

        decryption_layout.addLayout(decrypt_button_layout)

        return decryption_layout
    
    def _browse_file(self,line_edit) :
        file_path , _ = QFileDialog().getOpenFileName(self, 'Select File')
        if file_path :
            line_edit.setText(file_path)
    
    def _browse_encryption_key_file(self) -> None :
        self._browse_file(self.enc_key_file_line_edit)

    def _browse_encryption_input_file(self) -> None :
        self._browse_file(self.enc_input_file_line_edit)

    def _browse_encryption_output_folder(self) -> None :
        self._browse_file(self.enc_output_folder_line_edit)

    def _browse_decryption_key_file(self) -> None:
        self._browse_file(self.dec_key_file_line_edit)

    def _browse_decryption_input_file(self) -> None :
        self._browse_file(self.dec_input_file_line_edit)

    def _browse_decryption_output_folder(self) -> None :
        self._browse_file(self.dec_output_folder_line_edit)

    def _browse_generate_key_folder(self) -> None :
        self._browse_file(self.save_folder_line_edit)

    def _connect_signals(self) :

        self.save_folder_browse_button.clicked.connect(self._browse_generate_key_folder)

        self.enc_key_file_browse_button.clicked.connect(self._browse_encryption_key_file)
        self.enc_input_file_browse_button.clicked.connect(self._browse_encryption_input_file)
        self.enc_output_folder_browse_button.clicked.connect(self._browse_encryption_output_folder)

        self.dec_key_file_browse_button.clicked.connect(self._browse_decryption_key_file)
        self.dec_input_file_browse_button.clicked.connect(self._browse_decryption_input_file)
        self.dec_output_folder_browse_button.clicked.connect(self._browse_decryption_output_folder)
        