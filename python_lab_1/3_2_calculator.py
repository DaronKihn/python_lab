print("Введите 2 дробных числа и операцию, которую желаете применить к ним:")
a = float(input())
b = float(input())
operation = input()
if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/" and b != 0:
    print(a / b)
else:
    print("888888")