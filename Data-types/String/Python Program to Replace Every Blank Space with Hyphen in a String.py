def func(str1):
    res = ''
    for i in str1:
        if i == ' ':
            temp='-'
            res+=temp
        else:
            res+=i
    return res
str1 = input()
print(func(str1))
