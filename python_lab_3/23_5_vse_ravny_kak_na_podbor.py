def same_by(characteristic, objects):
    arr = list(filter(characteristic, objects))
    print(arr)
    if arr == objects:
        return True
    else:
        return False


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2 == 0, values):
    print('same')
else:
    print('different')
