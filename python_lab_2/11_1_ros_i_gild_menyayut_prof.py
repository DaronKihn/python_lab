text = input()
maxim = 0
dlina = 0
for i in range(len(text)):
    if text[i] == 'о':
        dlina += 1
    elif text[i] == 'р':
        if maxim < dlina:
            maxim = dlina
            dlina = 0
print(maxim)
