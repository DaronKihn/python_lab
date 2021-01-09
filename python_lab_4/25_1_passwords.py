from string import ascii_letters, digits
from random import choice
FORBIDDEN_SYMBOLS = {'l', 'I', '1', 'o', 'O', '0'}


def generate_password(m):
    password = []
    count = 0
    while count != m:
        symbol = choice(ascii_letters + digits)
        if symbol not in FORBIDDEN_SYMBOLS and symbol not in password:
            password += symbol
            count += 1
    return ''.join(password)


def main(n, m):
    return [generate_password(m) for i in range(n)]


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")

