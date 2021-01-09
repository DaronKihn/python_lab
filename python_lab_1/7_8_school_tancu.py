print("Введите запас терпения учителя:")
terp = int(input())
count_error = 0
count_correct = 0
exitLoop = False
while not exitLoop:
    if count_error < terp:
        stroka = input()
        if stroka == "раз":
            count_correct += 1
        else:
            count_error += 1
            if count_error < terp:
                print("Правильных отсчётов было ", count_correct, ", но теперь вы ошиблись.")
                count_correct = 0
                continue
            else:
                print("На сегодня хватит.")
                exit()
    else:
        print("На сегодня хватит.")
        exit()
    if count_error < terp:
        stroka = input()
        if stroka == "два":
            count_correct += 1
        else:
            count_error += 1
            if count_error < terp:
                print("Правильных отсчётов было ", count_correct, ", но теперь вы ошиблись.")
                count_correct = 0
                continue
            else:
                print("На сегодня хватит.")
                exit()
    else:
        print("На сегодня хватит.")
        exit()
    if count_error < terp:
        stroka = input()
        if stroka == "три":
            count_correct += 1
        else:
            count_error += 1
            if count_error < terp:
                print("Правильных отсчётов было ", count_correct, ", но теперь вы ошиблись.")
                count_correct = 0
                continue
            else:
                print("На сегодня хватит.")
                exit()
    else:
        print("На сегодня хватит.")
        exit()
    if count_error < terp:
        stroka = input()
        if stroka == "четыре":
            count_correct += 1
        else:
            count_error += 1
            if count_error < terp:
                print("Правильных отсчётов было ", count_correct, ", но теперь вы ошиблись.")
                count_correct = 0
                continue
            else:
                print("На сегодня хватит.")
                exit()
    else:
        print("На сегодня хватит.")
        exit()



