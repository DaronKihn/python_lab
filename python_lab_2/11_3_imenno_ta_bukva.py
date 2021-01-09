print("сообщение:")
message = input()
print("любимое число:")
number = int(input())
print("любимая буква:")
letter = input()
if number > len(message) or len(letter) != 1:
    print("ОШИБКА")
    exit()
if message[number - 1] == letter:
    print("ДА")
else:
    print("НЕТ")