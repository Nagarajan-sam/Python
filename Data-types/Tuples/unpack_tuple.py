def func(tuple1):
    res = 'a'
    for i in tuple1:
        if i in tuple1:
            print(res,"=",i)
            temp = ord(res) + 1
            res = chr(temp)
tuple1 = (10, 20, 30, 40)
func(tuple1)
