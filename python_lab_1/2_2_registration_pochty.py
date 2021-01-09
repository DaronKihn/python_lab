print("Введите логин:")
login = input()
print("Введите резервный адрес электронной почты:")
email = input()
if "@" not in login and "@" in email:
    print("OK")
elif "@" in login:
    print("Некорректный логин")
elif "@" not in email:
    print("Некорректный адрес")