def func(str):
    res = 0
    for i in str:
        if ('a'<=i<='z'):
            res+=1
    return res
str = input()
print(func(str))
