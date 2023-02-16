def func(t):
    tuple1 = list(t)
    for i in range(0,len(tuple1)): 
        for j in range(0, len(tuple1)-i-1):
            if (tuple1[j][1] > tuple1[j+1][1]):
                temp = tuple1[j]
                tuple1[j] = tuple1[j+1]
                tuple1[j+1] = temp
    return tuple1
t = (('a', 23),('b', 37),('c', 11), ('d',29))
print(func(t))
