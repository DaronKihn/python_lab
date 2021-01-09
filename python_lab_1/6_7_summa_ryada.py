print("Введите количество чисел:")
count = int(input())
total = 0
if count == 0:
    exit()
for i in range(count):
    number = int(input())
    if (i + 1) % 2 == 0:
        total -= number
    else:
        total += number
print(total)