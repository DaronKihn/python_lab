print("Введите количество натуральных чисел: ")
number = int(input())
total = 0
for i in range(number):
    obr_kv = 1 / (i + 1) ** 2
    total += obr_kv
print(3.141592653589793 ** 2 / total)
