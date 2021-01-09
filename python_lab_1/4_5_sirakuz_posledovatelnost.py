print("Введите натуральное число: ")
number = int(input())
count = 0
while number != 1:
    if number % 2 == 0:
        number /= 2
    else:
        number = 3 * number + 1
    count += 1
print(count)