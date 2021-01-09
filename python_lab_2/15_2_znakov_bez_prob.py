str = input()
count = str.count(' ') + str.count('\v') + str.count('\f') + str.count('\r') + str.count('\t') + str.count('\n')
print(len(str) - count)