print("Введите трехзначный код:")
number = int(input())
a = number % 10
number //= 10
b = number % 10
number //= 10
if a + b > b + number:
    print(str(a + b) + str(b + number))
else:
    print(str(b + number) + str(a + b))