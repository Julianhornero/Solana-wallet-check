from solana.publickey import PublicKey

def is_valid_solana_address(address: str) -> bool:
    try:
        pubkey = PublicKey(address)
        # Optional: check if the public key is on the Ed25519 curve
        # This excludes valid PDAs which are off-curve but you can skip this if you want
        return pubkey.is_on_curve()
    except Exception:
        return False

def bulk_validate_addresses(addresses):
    results = {}
    for addr in addresses:
        results[addr] = is_valid_solana_address(addr)
    return results

if __name__ == "__main__":
    addresses_to_check = [
        "4Nd1mJvV6q9pX5Q5rJrH1qT3Q1vXk6uY8q1f6f1J5XyK",  # example valid
        "invalidAddress123",
        "3N5x9T5xL1vG7F3xqX9T3L9vXk6uY8q1f6f1J5XyK9P"
    ]

    validation_results = bulk_validate_addresses(addresses_to_check)
    for addr, is_valid in validation_results.items():
        print(f"{addr}: {'Valid' if is_valid else 'Invalid'}")
