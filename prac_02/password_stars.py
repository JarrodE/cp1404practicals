MINIMUS_PASSWORD_LENGTH = 8

password = input("Password: ")
while len(password) < MINIMUS_PASSWORD_LENGTH:
    print(f"Invalid, must be more then {MINIMUS_PASSWORD_LENGTH} characters")
    password = input("Password: ")
print("*" * len(password))
