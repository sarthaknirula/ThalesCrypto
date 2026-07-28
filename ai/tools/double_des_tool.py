"""Double DES AI tool interface."""

from typing import Any

from crypto.double_des import DoubleDESService


class DoubleDESTool:
    """Thin adapter for Double DES service operations."""

    def __init__(self) -> None:
        """Create the Double DES service used by this tool."""
        self.service = DoubleDESService()
        self.operations = {
            "generate_key": self.service.generate_key,
            "encrypt": self.service.encrypt,
            "decrypt": self.service.decrypt,
        }

    def execute(self, operation: str, arguments: dict[str, Any]) -> Any:
        """Execute a Double DES operation with dispatcher-provided arguments."""
        method = self.operations.get(operation)
        if method is None:
            raise ValueError(f"Unsupported operation: {operation}")

        return method(**arguments)
