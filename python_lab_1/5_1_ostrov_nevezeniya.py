print("Введите день, месяц и год рождения аборигена:")
day = int(input())
month = int(input())
year = int(input())
c = year // 100
year %= 100
if month <= 2:
    month = month + 10
else:
    month = month - 2

print((day + ((13 * month - 1) // 5) + year + (year // 4 + c // 4 - 2 * c + 777)) % 7)