print("Введите количество сотрудников:")
count = int(input())
vse = set()
unikal = set()
print("Введите фамилии сотрудников:")
for i in range(count):
    surname = input()
    if surname not in vse:
        unikal.add(surname)
        vse.add(surname)
    elif surname in vse and surname in unikal:
        unikal.remove(surname)
print("Количество однофамильцев -", count - len(unikal))