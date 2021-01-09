print("Слово:")
text = input()
print("Номер буквы:")
number = int(input())
if number > len(text) or number < 1:
    print("ОШИБКА")
else:
    print("Буква -", text[number - 1])