def prime(number):
    i = 2
    while i * i <= number:
        if number % i == 0:
            return "Составное число"
        i += 1
    return "Простое число"


print("Введите число:")
print(prime(int(input())))