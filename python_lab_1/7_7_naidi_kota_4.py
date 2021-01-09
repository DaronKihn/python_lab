print("Введите количество строк:")
count = int(input())
flag = False
for i in range(count):
    stroka = input()
    if "Кот" in stroka or "кот" in stroka:
        flag = True
if flag:
    print("МЯУ")
else:
    print("НЕТ")
    __;______________________________
    ;