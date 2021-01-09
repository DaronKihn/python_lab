matrix = []
while True:
    line = input()
    if line:
        matrix.append(line.split())
    else:
        break
print(not all([int(matrix[i][j]) for i in range(len(matrix)) for j in range(len(matrix[i]))]))
