adress = input()
kluch = input()
adress_to_list = adress.split('?')
zapros_to_list = adress_to_list[1].split('&')
for elem in zapros_to_list:
    if kluch in elem:
        print(elem.split('=')[1])
