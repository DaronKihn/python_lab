print("Введите 17 чисел: ")
for i in range(17):
    number = int(input())
    if number == 0:
        exit()
    if i % number == 0:
        print("ДА")
    else:
        print("НЕТ")