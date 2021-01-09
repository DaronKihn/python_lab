bel_spis = list()
zaprosu = list()
print("Количество пунктов «белого списка»:")
number = int(input())
print("Введите пункты этого списка:")
for i in range(number):
    bel_spis.append(input())
print("Количество запросов, которые нужно проанализировать:")
number = int(input())
print("Введите запросы:")
for i in range(number):
    zaprosu.append(input())
print("Запросы из введённых, которые есть в «белом списке»:")
for z in zaprosu:
    if z in bel_spis:
        print(z)