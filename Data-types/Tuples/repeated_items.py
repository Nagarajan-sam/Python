def func(t1):
    y = []
    for i in t1:
        if t1.count(i) > 1:
            if i not in y:
                y.append(i)
    return tuple(y)    
t1 = (1,2,3,4,2,1)
print(func(t1))
