"""Shoon Lei Tun"""

MINIMUM_LENGTH = 4


def version_1():
    """Get a password of valid size and print asterisks."""
    password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))

    print('*' * len(password))
