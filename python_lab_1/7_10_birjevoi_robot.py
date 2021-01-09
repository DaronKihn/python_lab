s1 = int (input())
s2 = int(input())
flag_pokupka = False
flag_prodaja = False
while s1 != 0 and s2 != 0:
    if not flag_pokupka:
        if s2 > s1:
            price1 = s2
            flag_pokupka = True
    if flag_pokupka and not flag_prodaja:
        if s1 > s2:
            price2 = s2
            flag_prodaja = True
    s1 = s2
    s2 = int(input())
print(price1, price2, price2 - price1)