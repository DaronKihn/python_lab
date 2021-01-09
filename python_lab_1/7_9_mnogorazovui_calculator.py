exitLoop = False
while not exitLoop:
    str1 = int(input())
    str2 = input()
    if str2 == "+" or str2 == "-" or str2 == "*" or str2 == "/" or str2 == "%":
        str3 = int(input())
        if str2 == "+":
            print(str1 + str3)
        elif str2 == "-":
            print(str1 - str3)
        elif str2 == "*":
            print(str1 * str3)
        elif str2 == "/":
            if str3 == 0:
                continue
            print(str1 // str3)
        elif str2 == "%":
            if str3 == 0:
                continue
            print(str1 % str3)
    elif str2 == "!":
        if str1 < 0:
            continue
        res = 1
        while str1:
            res *= str1
            str1 -= 1
        print(res)
    elif str2 == "x":
        print(str1)
        exit()
