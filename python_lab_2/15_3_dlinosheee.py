str = input()
count = 1
max = 1
for i in range(len(str)-1):
    if str[i] == str[i+1]:
        count += 1
        if count > max:
            max = count
    else:
        count = 1
print(max)