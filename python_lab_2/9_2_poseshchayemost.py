print("Введите количество листков:")
count_list = int(input())
if count_list < 1:
    exit()
set1 = set()
set2 = set()
print("Введите количество учеников:")
count_person = int(input())
print("Введите фамилии учеников:")
for i in range(count_person):
    set1.add(input())
if count_list == 1:
    print("Фамилии учеников, посетивших все занятия:")
    for elem in set1:
        print(elem)
else:
    for i in range(count_list - 1):
        print("Введите количество учеников:")
        count_person = int(input())
        print("Введите фамилии учеников:")
        for j in range(count_person):
            set2.add(input())
        set1 = set1.intersection(set2)
        set2.clear()
print("Фамилии учеников, посетивших все занятия:")
for elem in set1:
    print(elem)
