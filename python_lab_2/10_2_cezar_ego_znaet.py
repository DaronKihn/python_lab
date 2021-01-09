print("Шаг:")
shag = int(input())
print("Послание:")
message = input()
zash_message = ""
for letter in message:
    if ord(letter) < 1040 or ord(letter) > 1103:
        zash_message += letter
    elif 1040 <= ord(letter) <= 1071:
        if ord(letter) + shag > 1071:
            zash_message += chr(ord(letter) + shag - 32)
        else:
            zash_message += chr(ord(letter) + shag)
    elif 1072 <= ord(letter) <= 1103:
        if ord(letter) + shag > 1103:
            zash_message += chr(ord(letter) + shag - 32)
        else:
            zash_message += chr(ord(letter) + shag)
print(zash_message)
