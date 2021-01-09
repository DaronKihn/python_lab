def encrypt_caesar(message, shift=3):
    zash_message = ""
    for letter in message:
        if ord(letter) < 1040 or ord(letter) > 1103:
            zash_message += letter
        elif 1040 <= ord(letter) <= 1071:
            if ord(letter) + shift > 1071:
                zash_message += chr(ord(letter) + shift - 32)
            else:
                zash_message += chr(ord(letter) + shift)
        elif 1072 <= ord(letter) <= 1103:
            if ord(letter) + shift > 1103:
                zash_message += chr(ord(letter) + shift - 32)
            else:
                zash_message += chr(ord(letter) + shift)
    return zash_message


def decrypt_caesar(message, shag=3):
    return encrypt_caesar(message, shag * (-1))


msg = "Да здравствует салат Цезарь!"
shift = 5
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)
