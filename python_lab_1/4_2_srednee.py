print("Введите температуру воздуха. В конце введите действительное число, меньшее -300")
count = 0
total = 0
temp = float(input())
while temp >= -300:
    total += temp
    count += 1
    temp = float(input())
if count == 0:
    print(0)
    exit()
print(total / count)

