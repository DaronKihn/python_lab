print("Введите целое число:")
number = int(input())
power = 1
a = 2
if number <= 0:
    print("НЕТ")
elif number == 1:
    print(0)
    exit()
while a < number:
    a *= 2
    power += 1
if a == number:
    print(power)
else:
    print("НЕТ")