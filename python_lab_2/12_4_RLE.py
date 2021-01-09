stroka = input()
count = 1
for i in range(len(stroka) - 1):
    if stroka[i + 1] == stroka[i]:
        count += 1
    else:
        print(count, stroka[i])
        count = 1
print(count, stroka[-1])
