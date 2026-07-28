"""Tests for AI tool adapters."""

import unittest
from unittest.mock import Mock

from ai.tools.aes_tool import AESTool
from ai.tools.double_des_tool import DoubleDESTool
from ai.tools.rsa_tool import RSATool
from ai.tools.triple_des_tool import TripleDESTool


class ToolAdapterTests(unittest.TestCase):
    """Verify AI tools dispatch operations to crypto services."""

    def test_unsupported_operation_raises_value_error(self) -> None:
        """Unsupported operations should fail before calling a service."""
        tool = AESTool()

        with self.assertRaisesRegex(ValueError, "Unsupported operation: rotate"):
            tool.execute("rotate", {})

    def test_aes_encrypt_dispatches_to_service(self) -> None:
        """AES encrypt should call AESService.encrypt."""
        tool = AESTool()
        tool.service.encrypt = Mock(return_value="encrypted")
        arguments = {
            "key_path": "aes.key",
            "input_file_path": "plain.txt",
            "output_folder": "out",
        }

        result = tool.execute("encrypt", arguments)

        self.assertEqual(result, "encrypted")
        tool.service.encrypt.assert_called_once_with(**arguments)

    def test_aes_decrypt_dispatches_to_service(self) -> None:
        """AES decrypt should call AESService.decrypt."""
        tool = AESTool()
        tool.service.decrypt = Mock(return_value="decrypted")
        arguments = {
            "key_path": "aes.key",
            "input_file_path": "plain.txt.aes.enc",
            "output_folder": "out",
        }

        result = tool.execute("decrypt", arguments)

        self.assertEqual(result, "decrypted")
        tool.service.decrypt.assert_called_once_with(**arguments)

    def test_rsa_generate_key_pair_dispatches_to_service(self) -> None:
        """RSA generate_key_pair should call RSAService.generate_key_pair."""
        tool = RSATool()
        tool.service.generate_key_pair = Mock(
            return_value=("public.pem", "private.pem")
        )
        arguments = {"key_length": 4096, "save_directory": "keys"}

        result = tool.execute("generate_key_pair", arguments)

        self.assertEqual(result, ("public.pem", "private.pem"))
        tool.service.generate_key_pair.assert_called_once_with(**arguments)

    def test_double_des_encrypt_dispatches_to_service(self) -> None:
        """Double DES encrypt should call DoubleDESService.encrypt."""
        tool = DoubleDESTool()
        tool.service.encrypt = Mock(return_value="double-des-encrypted")
        arguments = {
            "key1_path": "key1.key",
            "key2_path": "key2.key",
            "input_file_path": "plain.txt",
            "output_folder": "out",
        }

        result = tool.execute("encrypt", arguments)

        self.assertEqual(result, "double-des-encrypted")
        tool.service.encrypt.assert_called_once_with(**arguments)

    def test_triple_des_decrypt_dispatches_to_service(self) -> None:
        """Triple DES decrypt should call TripleDESService.decrypt."""
        tool = TripleDESTool()
        tool.service.decrypt = Mock(return_value="triple-des-decrypted")
        arguments = {
            "key1_path": "key1.key",
            "key2_path": "key2.key",
            "key3_path": "key3.key",
            "encrypted_file_path": "plain.txt.triple_des.enc",
            "output_folder": "out",
        }

        result = tool.execute("decrypt", arguments)

        self.assertEqual(result, "triple-des-decrypted")
        tool.service.decrypt.assert_called_once_with(**arguments)


if __name__ == "__main__":
    unittest.main()
