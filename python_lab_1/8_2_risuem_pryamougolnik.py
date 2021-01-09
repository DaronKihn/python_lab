print("Высота:")
height = int(input())
print("Ширина:")
width = int(input())
print("Знак:")
symbol = input()
if height <= 1 or width <= 1:
    exit()
for i in range(height):
    if i == 0 or i == (height - 1):
        print(symbol * width)
    else:
        print(symbol + " " * (width - 2) + symbol)
