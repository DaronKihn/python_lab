count = int(input())
str = [input() for i in range(count)]
print(', '.join(str[i] for i in range(count) if "лук" not in str[i]))