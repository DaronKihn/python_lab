print('Введите размер квадратного поля(>=3)')
n = int(input())
print('Введите числа, описывающие колво бактерий в каждой клетке')
description = [[int(input()) for i in range(n)] for j in range(n)]
print('Введите колво капель антибиотика')
k = int(input())
for i in range(k):
    print('Введите столбец, куда попала капля')
    y0 = int(input())
    print('Введите ряд, куда попала капля')
    x0 = int(input())
    for x in range(n):
        for y in range(n):
            if x0 == x and y0 == y:
                description[x][y] -= 8
            elif (x == x0 - 1 and y == y0) or (x == x0 + 1 and y == y0) or (y == y0 - 1 and x == x0) \
                    or (y == y0 + 1 and x == x0):
                description[x][y] -= 4
            elif (x == x0 - 1 and y == y0 - 1) or (x == x0 - 1 and y == y0 + 1) \
                    or (x == x0 + 1 and y == y0 - 1) or (x == x0 + 1 and y == y0 + 1):
                description[x][y] -= 4
for x0 in range(n):
    for y0 in range(n):
        if description[x0][y0] < 0:
            description[x0][y0] = 0
print('Колво бактерий, выживших в каждой клетке')
for i in description:
    print(*i)