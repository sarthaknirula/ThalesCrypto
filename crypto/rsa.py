from pathlib import Path
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

PROJECT_ROOT = Path(__file__).resolve().parents[1]


class RSAService() :
    VALID_KEY_SIZES = (2048,3072,4096)
    def generate_key_pair(self,key_length : int , save_directory : Path | None = None) -> tuple[Path, Path] :
        self._validate_key_size(key_length)
        if save_directory is None:
            save_directory = PROJECT_ROOT / "storage" / "keys"
        else:
            save_directory = Path(save_directory)

        save_directory.mkdir(parents=True, exist_ok=True)

        private_key, public_key = self._generate_keys(key_length)
        private_ser = self._serialize_private_key(private_key)
        public_ser = self._serialize_public_key(public_key)

        private_key_path = self._save_key(save_directory / "private_key.pem", private_ser)
        public_key_path = self._save_key(save_directory / "public_key.pem", public_ser)

        return public_key_path, private_key_path


    def _validate_key_size(self,key_length : int) -> None: 
        if key_length not in RSAService.VALID_KEY_SIZES :
            raise ValueError(f'Invalid key size {key_length}. Key size must be 2048 or 3072 or 4096.')
        
    def _generate_keys(self,key_length : int , public_exponent = 65537) :
        private_key = rsa.generate_private_key(public_exponent=public_exponent,key_size=key_length)
        public_key = private_key.public_key()

        return (private_key,public_key)
    
    def _serialize_private_key(self,private_key) -> bytes :
        private_ser = private_key.private_bytes(encoding = serialization.Encoding.PEM,
                                                format = serialization.PrivateFormat.PKCS8,
                                                encryption_algorithm = serialization.NoEncryption())
        
        return private_ser
    
    def _serialize_public_key(self,public_key) -> bytes:
        public_ser = public_key.public_bytes(encoding = serialization.Encoding.PEM,
                                             format = serialization.PublicFormat.SubjectPublicKeyInfo)

        return public_ser
    
    def _save_key(self, file_path : Path , key_bytes : bytes) -> Path:
        with file_path.open('wb') as f:
            f.write(key_bytes)
            
        return file_path

        
