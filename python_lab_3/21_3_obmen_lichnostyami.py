def swap(first, second):
    for i in range(len(first)):
        first[i], second[i] = second[i], first[i]


f = [1, 2, 3]
s = [4, 5, 6]
print(f, s)
swap(f, s)
print(f, s)
