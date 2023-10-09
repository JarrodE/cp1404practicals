"""Program that prompts user for 5 numbers and then stores each
of these in a list"""


def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    user_input = get_username()
    check_username(user_input, usernames)


def check_username(user_input, usernames):
    if user_input in usernames:
        print("Access granted")
    else:
        print("Access denied")


def get_username():
    user_input = input("Enter username: ")
    return user_input


main()
