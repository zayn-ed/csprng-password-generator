# CSPRNG Local Password Generator

A lightweight, cryptographically secure local password generator built in Python using OS hardware entropy (`secrets` module). Zero network calls, zero logging, 100% offline security.

## Key Features
- **Cryptographically Secure:** Uses system-level entropy via Python's `secrets` module (CSPRNG).
- **Policy Guaranteed:** Ensures generated passwords contain a mix of uppercase, lowercase, numbers, and special symbols.
- **Unbiased Shuffling:** Applies CSPRNG Fisher-Yates shuffling to eliminate positional bias.
- **Zero External Dependencies:** Built purely with standard Python modules.

## Getting Started

### Prerequisites
- Python 3.8 or higher installed locally.

### Execution

Clone the repository and run the generator:

```bash
git clone [https://github.com/zayn-ed/csprng-password-generator.git](https://github.com/zayn-ed/csprng-password-generator.git)
cd csprng-password-generator
python3 csprng-password-generator.py
