print('Приветствую вас на нашей викторине! В качестве ответа введите цифру выбранного варианта.')
count_of_correct = 0
print('Вопрос 1. Что Карлсон любил есть больше всего на свете?\n' + '1 - печенье и варенье\n' +
      '2 - шпроты в масле\n' + '3 - блины\n' + '4 - котлеты')
answer_1 = input()
if answer_1 == "1":
    count_of_correct += 1
elif answer_1 != "2" and answer_1 != "3" and answer_1 != "4":
    print("Ошибка")
    exit()
print('Вопрос 2. Что дала ведьма Белоснежке?\n' + '1 - отравленное яблоко\n' + '2 - печенье\n' +
      '3 - торт\n' + '4 - зелье\n' + '5 - орехи')
answer_2 = input()
if answer_2 == "1":
    count_of_correct += 1
elif answer_2 != "2" and answer_2 != "3" and answer_2 != "4" and answer_2 != "5":
    print("Ошибка")
    exit()
print('Вопрос 3. Что попросил старик у золотой рыбки во второй раз?\n' + '1 - избу\n' + '2 - новую жену\n' +
      '3 - деньги')
answer_3 = input()
if answer_3 == "1":
    count_of_correct += 1
elif answer_3 != "2" and answer_3 != "3":
    print("Ошибка")
    exit()
print('Вопрос 4. Где обычно сидела любимая крыса Шапокляк?\n' + '1 - в кармане\n' + '2 - в сумочке\n' +
      '3 - на плече\n' + '4 - на голове\n')
answer_4 = input()
if answer_4 == "2":
    count_of_correct += 1
elif answer_2 != "1" and answer_2 != "3" and answer_2 != "4":
    print("Ошибка")
    exit()
if count_of_correct == 4:
    print("Вы обладаете незаурядным умом!")
elif count_of_correct == 3:
    print("Вы эрудированный человек!")
elif count_of_correct == 2:
    print("Вы молодец!")
elif count_of_correct == 1:
    print("Думаю, в следующий раз у вас получится лучше!")
else:
    print("Потренируйтесь и приходите снова. У вас все получится!")