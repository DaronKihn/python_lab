from string import ascii_uppercase, ascii_lowercase, ascii_letters, digits
from random import choice, random
FORBIDDEN_SYMBOLS = {'l', 'I', '1', 'o', 'O', '0'}


def generate_password(m):
    password = []
    count = 0
    while True:
        symbol = choice(ascii_uppercase)
        if symbol not in FORBIDDEN_SYMBOLS and symbol not in password:
            password += symbol
            count += 1
        if count == 1:
            break
    while True:
        symbol = choice(ascii_lowercase)
        if symbol not in FORBIDDEN_SYMBOLS and symbol not in password:
            password += symbol
            count += 1
        if count == 2:
            break
    while True:
        symbol = choice(digits)
        if symbol not in FORBIDDEN_SYMBOLS and symbol not in password:
            password += symbol
            count += 1
        if count == 3:
            break
    while count != m:
        symbol = choice(ascii_letters + digits)
        if symbol not in FORBIDDEN_SYMBOLS and symbol not in password:
            password += symbol
            count += 1
    password = sorted(password, key=lambda x: random())
    return ''.join(password)


def main(n, m):
    return [generate_password(m) for i in range(n)]


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
