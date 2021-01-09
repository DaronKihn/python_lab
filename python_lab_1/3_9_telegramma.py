print("Введите сообщение:")
message = input()
print(len(message) * 40 // 100, "руб. ", len(message) * 40 % 100, "коп.")