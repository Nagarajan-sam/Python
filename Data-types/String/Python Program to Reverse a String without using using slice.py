def func(str1):
    res = ''
    for i in str1:
        res = i + res
    return res
str1 = input()
print(func(str1))
