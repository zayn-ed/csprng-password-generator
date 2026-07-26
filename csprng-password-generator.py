import secrets
import string


def generate_password(
    length: int = 16,
    use_uppercase: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True
) -> str:
    """
    Generates a cryptographically secure random password.
    
    Guarantees at least one character from each enabled character pool
    and shuffles using system-level entropy.
    """
    if length < 8:
        raise ValueError("Password length must be at least 8 characters for security.")

    # 1. Assemble selected character sets
    pools = [string.ascii_lowercase]  # Lowercase is always enabled
    if use_uppercase:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append("!@#$%^&*()_+-=[]{}|;:,.<>?")

    # 2. Guarantee complexity (at least 1 character from every active pool)
    password = [secrets.choice(pool) for pool in pools]

    # 3. Fill the remaining positions from the combined pool
    all_characters = "".join(pools)
    remaining_length = length - len(password)
    password.extend(secrets.choice(all_characters) for _ in range(remaining_length))

    # 4. Perform an unbiased, CSPRNG-powered Fisher-Yates shuffle
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


if __name__ == "__main__":
    try:
        # Example: Generate a 16-character secure password
        secure_password = generate_password(
            length=16,
            use_uppercase=True,
            use_digits=True,
            use_symbols=True
        )
        print(f"Generated Password: {secure_password}")
    except ValueError as error:
        print(f"Error: {error}")