dictionary = {}
print('Введите колво номеров телефонов')
n = int(input())
print('Введите через пробел: телефон, имя(состоит из русских букв)')

for _ in range(n):
    number, name = input().split()
    if name in dictionary:
        dictionary[name].append(number)
    else:
        dictionary[name] = [number]
print('Введите колво запросов')
m = int(input())
print('Введите сами запросы(имя друга)')
for _ in range(m):
    request = input()
    print(*dictionary.get(request, ['Нет в телефонной книге']))