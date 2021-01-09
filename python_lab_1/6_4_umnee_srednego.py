print("Введите кол-во человек:")
count = int(input())
total = 0
for i in range(count):
    print("Введите IQ")
    iq = int(input())
    total += iq
    if iq > total / (i + 1):
        print(">")
    elif iq < total / (i + 1):
        print("<")
    elif iq == total / (i + 1):
        print("0")
