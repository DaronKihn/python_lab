bluda = set()
print("Количество блюд:")
count_blud = int(input())
if count_blud == 0:
    exit()
print("Названия блюд:")
for i in range(count_blud):
    bluda.add(input())
print("Число дней, для которых есть списки блюд:")
count_dney = int(input())
for i in range(count_dney):
    print("Число блюд в данный день:")
    count_blud_den = int(input())
    print("Перечислите эти блюда:")
    for j in range(count_blud_den):
        name = input()
        bluda.discard(name)
if len(bluda) == 0:
    print("Нет блюд, которые ещё ни разу не готовили.")
else:
    print("Список блюд, которые ещё ни разу не готовили:")
    for elem in bluda:
        print(elem)