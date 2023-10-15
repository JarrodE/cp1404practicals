"""
Emails
Estimated: 45 minutes
Actual: 50 minutes
"""


def main():
    """Collects email addresses and names and prints the list."""
    name_to_email = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        name_to_email.append((name, email))
        email = input("Email: ")

    for name, email in name_to_email.items():
        print(f"{name} ({email}")


def extract_name(email):
    """Extracts a name from an email address."""
    parts = email.split('@')
    name = parts[0].replace('.', ' ').title()
    return name


def get_name_from_email(email):
    """Asks user to confirm their name based on email address."""
    name = extract_name(email)
    choice = input(f"Is your name {name}? (Y/n) ").strip().lower()
    if choice == "" or choice == "y":
        return name
    else:
        user_name = input("Name: ")
        return user_name


main()
