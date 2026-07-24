"""Gemini chat service for the Thales Crypto desktop application."""

import os
from typing import Any

from google import genai
from google.genai import types

from core import settings

from .prompts import SYSTEM_PROMPT


class AIService:
    """Manage a persistent Gemini chat session and return raw responses."""

    DEFAULT_MODEL = settings.GEMINI_MODEL
    DEFAULT_TEMPERATURE = settings.GEMINI_TEMPERATURE

    def __init__(self) -> None:
        """Configure the Gemini client and start a persistent chat session."""
        self.client: genai.Client | None = None
        self.chat_session: Any | None = None
        self.model_name = self.DEFAULT_MODEL

        self._configure_client()
        self._start_chat()

    def _configure_client(self) -> None:
        """Create the Gemini client using the GEMINI_API_KEY environment variable."""
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY environment variable is not set.")

        self.client = genai.Client(api_key=api_key)

    def _start_chat(self) -> None:
        """Start a persistent Gemini chat session."""
        if self.client is None:
            raise RuntimeError("Gemini client is not configured.")

        self.chat_session = self.client.chats.create(
            model=self.model_name,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=self.DEFAULT_TEMPERATURE,
            ),
        )

    def generate_response(self, user_message: str) -> str:
        """Send a user message to Gemini and return the raw response text."""
        if self.chat_session is None:
            raise RuntimeError("Gemini chat session is not started.")

        try:
            response = self.chat_session.send_message(user_message)
            return response.text or ""
        except Exception as exc:
            raise RuntimeError(f"Gemini request failed: {exc}") from exc
