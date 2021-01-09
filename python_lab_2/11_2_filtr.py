print("Количество строк:")
n = int(input())
for i in range(n):
    text = input()
    if text[0] == "%" and text[1] == "%":
        print(text[2:])
    elif text[0] == "#" and text[1] == "#" and text[2] == "#" and text[3] == "#":
        continue
    else:
        print(text)