
def ask_password(str):
    if str == "password":
        print("Пароль принят")
        return True
    else:
        print("В доступе отказано")
        return False


flag = False
i = 0
while not flag and i < 3:
    print("Введите пароль:")
    flag = ask_password(input())
    i += 1
