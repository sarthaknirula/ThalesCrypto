"""RSA AI tool interface."""

from typing import Any

from crypto.rsa import RSAService


class RSATool:
    """Thin adapter for RSA service operations."""

    def __init__(self) -> None:
        """Create the RSA service used by this tool."""
        self.service = RSAService()
        self.operations = {
            "generate_key": self.service.generate_key_pair,
            "encrypt": self.service.encrypt_file,
            "decrypt": self.service.decrypt_file,
        }

    def execute(self, operation: str, arguments: dict[str, Any]) -> Any:
        """Execute an RSA operation with dispatcher-provided arguments."""
        method = self.operations.get(operation)
        if method is None:
            raise ValueError(f"Unsupported operation: {operation}")

        return method(**arguments)
