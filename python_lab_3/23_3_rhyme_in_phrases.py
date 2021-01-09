def number_of_vowels(word):
    vowels = {'ю', 'о', 'и', 'е', 'у', 'ы', 'э', 'а', 'я', 'ё', 'А', 'Е', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я', 'Ё'}
    return len(list(filter(lambda x: x in vowels, word)))


def rhyme(text):
    phrases = text.split()
    number_of_slogs = [number_of_vowels(elem) for elem in phrases]
    for i in range(1, len(number_of_slogs)):
        if number_of_slogs[i] == number_of_slogs[0]:
            if i == len(number_of_slogs) - 1:
                print("Парам пам-пам")
        else:
            print("Пам парам")
            exit()


text1 = "пара-ра-рам рам-пам-папам па-ра-па-дам"
text2 = "пара-ра рам-пам-папам па-ра-па-дам"
rhyme(text1)
rhyme(text2)
