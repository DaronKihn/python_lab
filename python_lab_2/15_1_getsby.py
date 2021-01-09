symb = input()
str = input()
str_to_list = str.split(" ")
for elem in str_to_list:
    if symb.lower() in elem or symb.upper() in elem:
        print(elem)