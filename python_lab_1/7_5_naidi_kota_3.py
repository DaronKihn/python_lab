exitLoop = False
naiden_kot = False
count_str = 0
perv_vh = 0
count_cat = 0
while not exitLoop:
    stroka = input()
    count_str += 1
    if ("Кот" in stroka or "кот" in stroka) and not naiden_kot:
        perv_vh = count_str
        naiden_kot = True
        count_cat += 1
    elif "Кот" in stroka or "кот" in stroka:
        count_cat += 1
    if stroka == "СТОП":
        break
if naiden_kot:
    print(count_cat, perv_vh)
else:
    print(count_cat, -1)

