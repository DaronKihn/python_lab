exitLoop = False
naiden_kot = False
count = 0
perv_vh = 0
while not exitLoop:
    stroka = input()
    count += 1
    if ("Кот" in stroka or "кот" in stroka) and not naiden_kot:
        perv_vh = count
        naiden_kot_kot = True
    if stroka == "СТОП":
        break
if naiden_kot:
    print(perv_vh)
else:
    print(-1)

