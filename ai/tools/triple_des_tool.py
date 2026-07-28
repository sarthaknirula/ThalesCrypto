"""Triple DES AI tool interface."""

from typing import Any

from crypto.triple_des import TripleDESService


class TripleDESTool:
    """Thin adapter for Triple DES service operations."""

    def __init__(self) -> None:
        """Create the Triple DES service used by this tool."""
        self.service = TripleDESService()
        self.operations = {
            "generate_key": self.service.generate_key,
            "encrypt": self.service.encrypt,
            "decrypt": self.service.decrypt,
        }

    def execute(self, operation: str, arguments: dict[str, Any]) -> Any:
        """Execute a Triple DES operation with dispatcher-provided arguments."""
        method = self.operations.get(operation)
        if method is None:
            raise ValueError(f"Unsupported operation: {operation}")

        return method(**arguments)
