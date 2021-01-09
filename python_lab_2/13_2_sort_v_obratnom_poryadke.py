numbers = []
print("Количество чисел:")
n = int(input())
print("Введите числа:")
for i in range(n):
    numbers.append(int(input()))
numbers.sort()
numbers.reverse()
for elem in numbers:
    print(elem)