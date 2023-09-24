MINIMUS_PASSWORD_LENGTH = 8


def main():
    """Get password and check it's length. Prints asterisks the length of password."""
    password = get_password()
    while len(password) < MINIMUS_PASSWORD_LENGTH:
        print(f"Invalid, must be more then {MINIMUS_PASSWORD_LENGTH} characters")
        password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """Print asterisks the length of password."""
    print("*" * len(password))


def get_password():
    """Get user password."""
    password = input("Password: ")
    return password


main()
