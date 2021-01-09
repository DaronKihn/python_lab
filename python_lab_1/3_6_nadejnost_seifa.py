print("Введите трехзначный код:")
number = int(input())
a = number % 10
number //= 10
b = number % 10
number //= 10
if a == b and b == number:
    print("В числе все цифры одинаковые")
elif a == b or a == number or b == number:
    print("В числе две одинаковые цифры")
else:
    print("ОК")