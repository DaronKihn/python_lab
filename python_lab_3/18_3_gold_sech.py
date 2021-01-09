def golden_ratio(i):
    number1 = 1
    number2 = 1
    for i in range(3, i + 2):
        number1, number2 = number2, number1 + number2
    return number2 / number1


print(golden_ratio(int(input())))