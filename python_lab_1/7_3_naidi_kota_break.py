print("Введите количество строк:")
count = int(input())
for i in range(count):
    stroka = input()
    if "Кот" in stroka or "кот" in stroka:
        print("МЯУ")
        break
    elif i == (count - 1):
        print("НЕТ")
