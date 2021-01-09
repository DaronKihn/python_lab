print('Введите число рядов таблицы')
R = int(input())
print('Введите строки этой таблицы')
rows = [input().split(',') for _ in range(R)]
print('Введите число элементов таблицы, которые надо вывести')
n = int(input())
print('Введите разделенные запятой координаты элементов таблицы(строка, столбец)')
for j in range(n):
    row_number, column_number = [int(i) for i in input().split(',')]
    print(rows[row_number][column_number])