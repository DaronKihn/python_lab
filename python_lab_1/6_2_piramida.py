print("Введите количество уровней пирамиды:")
floor = int(input())
count = 0
while count < floor:
    count_pr = ((2 * (floor - 1) + 1) - (2 * count + 1)) / 2
    count_zv = 2 * count + 1
    print(" " * int(count_pr) + "*" * int(count_zv) + " " * int(count_pr))
    count += 1