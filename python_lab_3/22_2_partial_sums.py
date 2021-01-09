def partial_sums(*args):
    print(args)
    lst = [0]
    for i in range(len(args)):
        sums = 0
        for j in range(i + 1):
            sums += args[j]
        lst.append(sums)
    return lst


print(*partial_sums(1, 0.5, 0.25, 0.125))
