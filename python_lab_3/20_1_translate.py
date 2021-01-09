SIGNS = {'.', ',', ':', ';', '-', '?', '!'}
VOWELS = {'ю', 'о', 'и', 'е', 'у', 'ы', 'э', 'а', 'я', 'ё', 'А', 'Е', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я', 'Ё'}


def translate(text):
    new_text = ""
    for i in range(len(text)):
        if len(new_text) != 0:
            if new_text[-1] == " " and text[i] == " ":
                continue
        if text[i] in SIGNS or text[i] in VOWELS:
            continue
        else:
            new_text += text[i]
    return new_text


translatedText = None
translatedText = translate("Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно \
                            просто читать. Достаточно небольшой тренировки - и вы сможете это делать.")
print(translatedText)
