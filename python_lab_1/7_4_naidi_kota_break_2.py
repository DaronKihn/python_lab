exitLoop = False
count = 0
while not exitLoop:
    stroka = input()
    count += 1
    if "Кот" in stroka or "кот" in stroka:
        print(count)
        break
    if stroka == "СТОП":
        print(-1)
        break
