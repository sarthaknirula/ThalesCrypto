# Thales Crypto

Thales Crypto is a desktop application built with **Python** and **PySide6** that provides modern cryptographic utilities through a clean graphical interface. The project focuses on modular architecture, separation of concerns, and extensibility. It also includes the foundation of an AI-powered assistant that will help users understand and perform cryptographic operations.

> **Project Status:** 🚧 Under Active Development

---

# Current Features

## Encryption Algorithms

### AES
- File Encryption
- File Decryption
- Secure Key Generation

### RSA
- RSA Key Pair Generation
- Encryption
- Decryption

### Double DES
- File Encryption
- File Decryption
- Key Generation

### Triple DES
- File Encryption
- File Decryption
- Key Generation

---

# AI Assistant (In Progress)

The project includes the initial implementation of an AI assistant powered by the Gemini API.

Current progress includes:

- Gemini API integration
- Persistent chat session
- Prompt engineering
- Modular AI architecture
- Dedicated AI service layer

The AI assistant is designed to:

- Explain cryptographic concepts
- Recommend suitable encryption algorithms
- Understand user intent
- Return structured JSON responses for application actions

The AI **does not perform cryptographic operations directly**. Instead, it delegates operations to the existing cryptographic service layer.

---

# Architecture

The application follows a layered architecture.

```text
GUI

↓

Service Layer

↓

Cryptographic Operations

↓

Filesystem
```

Each feature follows the same design philosophy.

Example:

```text
AES Page

↓

AES Service

↓

Storage
```

---

# AI Architecture

The AI module follows the architecture below.

```text
User

↓

AI Page

↓

AI Service

↓

Gemini API

↓

Structured JSON

↓

Parser

↓

Dispatcher

↓

Tools

↓

Cryptographic Services
```

This design keeps responsibilities clearly separated and allows the AI system to grow independently of the cryptographic implementation.

---

# Project Structure

```text
ThalesCrypto/

├── ai/
│   ├── dispatcher.py
│   ├── parser.py
│   ├── prompts.py
│   ├── service.py
│   └── tools/
│
├── assets/
├── core/
├── crypto/
├── gui/
├── storage/
├── tests/
│
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

# Technologies Used

- Python
- PySide6
- Google Gemini API
- Cryptography Library

---

# Installation

Clone the repository.

```bash
git clone <repository-url>
cd ThalesCrypto
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the virtual environment.

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

---

# Gemini API Configuration

Generate a Gemini API key from Google AI Studio.

Export the API key as an environment variable.

### Linux / macOS

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

### Windows

```cmd
set GEMINI_API_KEY=YOUR_API_KEY
```

The application automatically loads the API key from the environment.

---

# Running the Application

```bash
python app.py
```

---

# Running AI Service Tests

An interactive test is available for manually testing the AI service.

```bash
python tests/test_ai_service.py
```

---

# Design Principles

The project is built around the following principles:

- Separation of Concerns
- Single Responsibility Principle
- Modular Design
- Maintainability
- Extensibility
- Clean Architecture

---

# Future Improvements

## AI Assistant

- JSON response parser
- Dispatcher implementation
- Tool execution layer
- AI-powered workflow automation
- Context-aware conversations
- Conversation history
- Better prompt engineering

## Cryptography

- Digital Signatures
- Hashing Algorithms
- HMAC Support
- Secure File Hash Verification
- Certificate Management
- Hybrid Encryption (AES + RSA)

## Application

- File drag-and-drop support
- Recent operations history
- User preferences
- Theme customization
- Logging system
- Better error reporting
- Plugin architecture
- Improved key management
- Secure key vault

---

# License

This project is intended for educational and learning purposes.