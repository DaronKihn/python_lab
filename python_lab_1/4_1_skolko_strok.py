print('Введите свои сообщения. В конце введите "Спасибо."')
message = input()
count_str = 1
while message != "Спасибо.":
    message = input()
    count_str += 1
print(count_str)