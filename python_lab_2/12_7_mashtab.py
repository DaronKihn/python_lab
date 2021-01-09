count_str = int(input())
count_stolb = int(input())
new_str = ""
mn_new_str = set()
for i in range(count_str):
    str = input()
    if i % 2 == 1:
        continue
    for j in range(count_stolb):
        if j % 2 == 1:
            continue
        else:
            new_str += str[j]
    mn_new_str.add(new_str)
    new_str = ""
for elem in mn_new_str:
    print(elem)
