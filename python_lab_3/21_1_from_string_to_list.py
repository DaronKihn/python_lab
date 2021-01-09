def from_string_to_list(string, container):
    for elem in string.split(" "):
        container.append(int(elem))


# a = [1, 4, 5]
# from_string_to_list("33 45 9", a)
# print(a)

