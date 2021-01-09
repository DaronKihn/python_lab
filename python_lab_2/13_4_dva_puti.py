brat1 = []
brat2 = []
count_pok = int(input())
for i in range(count_pok):
    pok = int(input())
    brat1.append(pok)
    brat2.append(pok)
count_tren = int(input())
for i in range(count_tren):
    brat = int(input())
    if brat == 1:
        brat1[int(input())] += int(input())
    else:
        brat2[int(input())] += int(input())
count_sovp = 0
for i in range(count_pok):
    if brat1[i] == brat2[i]:
        count_sovp += 1
print(brat1)
print(brat2)
print(count_sovp)

