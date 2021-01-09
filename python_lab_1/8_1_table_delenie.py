print("Количество столбцов:")
stolb = int(input())
print("Количество строк:")
strok = int(input())
for i in range(strok):
    for j in range(stolb):
        print((j + 1) / (i + 1), end=" ")
    print(end="\n")