words = []
while True:
    line = input()
    if line:
        words.append(line)
    else:
        break
print(*sorted(words, key=lambda word: sum([ord(i) - ord('A') + 1 for i in word.upper()])), sep='\n')

