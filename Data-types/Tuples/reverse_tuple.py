def func(t1):
    res=()
    for i in range(len(t1)-1,-1,-1):
        res = res + (t1[i],)
    return res
t1 = (10,20,30,40,50)
print(func(t1))
