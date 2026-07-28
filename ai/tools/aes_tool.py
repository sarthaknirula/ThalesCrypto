"""AES AI tool interface."""

from typing import Any

from crypto.aes import AESService


class AESTool:
    """Thin adapter for AES service operations."""

    def __init__(self) -> None:
        """Create the AES service used by this tool."""
        self.service = AESService()
        self.operations = {
            "generate_key": self.service.generate_key,
            "encrypt": self.service.encrypt,
            "decrypt": self.service.decrypt,
        }

    def execute(self, operation: str, arguments: dict[str, Any]) -> Any:
        """Execute an AES operation with dispatcher-provided arguments."""
        method = self.operations.get(operation)
        if method is None:
            raise ValueError(f"Unsupported operation: {operation}")

        return method(**arguments)
