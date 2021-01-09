print("Введите пароль:")
password = input()
if len(password) < 8:
    print("Короткий!")
    exit()
elif "123" in password:
    print("Простой!")
    exit()
print("Повторите пароль:")
password_2 = input()
if password == password_2:
    print("ОК")
else:
    print("Пароли различаются")