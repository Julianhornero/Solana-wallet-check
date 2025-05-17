
# Solana-wallet-check

Bulk Validate Solana Addresses using Python

---

## Overview

This project provides a simple Python script to bulk validate Solana wallet addresses. It checks whether each address is a valid Solana public key and optionally verifies if it lies on the Ed25519 curve.

---

## Features

- Validate multiple Solana wallet addresses in bulk.
- Uses the official `solana` Python library.
- Simple and easy to use.
- Outputs validation results for each address.

---

## Requirements

- Python 3.6 or higher
- `solana` Python package

---

## Installation

1. Clone the repository:

```
git clone https://github.com/Julianhornero/Solana-wallet-check.git
cd Solana-wallet-check
```

2. Install dependencies:

```
pip install solana
```

---

## Usage

Edit the `sl.py` script or create your own script to input the list of Solana addresses you want to validate.

Example usage in `sl.py`:

```
from solana.publickey import PublicKey

def is_valid_solana_address(address: str) -> bool:
    try:
        pubkey = PublicKey(address)
        return pubkey.is_on_curve()
    except Exception:
        return False

addresses = [
    "4Nd1mJvV6q9pX5Q5rJrH1qT3Q1vXk6uY8q1f6f1J5XyK",
    "invalidAddress123",
    "3N5x9T5xL1vG7F3xqX9T3L9vXk6uY8q1f6f1J5XyK9P"
]

for addr in addresses:
    print(f"{addr}: {'Valid' if is_valid_solana_address(addr) else 'Invalid'}")
```

Run the script:

```
python sl.py
```

---

## Notes

- This validation checks the format and curve compliance of Solana addresses.
- It does not verify whether an address exists on the blockchain or has any balance.
- For on-chain data, consider integrating with Solana RPC endpoints or third-party APIs.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

