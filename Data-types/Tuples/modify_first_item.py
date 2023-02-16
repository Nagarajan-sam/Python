def func(tuple1):
    temp = list(tuple1)
    temp[1][0] = 22
    return tuple(temp)
tuple1 = (11, [11, 33], 44, 55)
print(func(tuple1))
