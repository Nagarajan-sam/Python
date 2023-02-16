def func(str1,str2):
    s = (str1)+(str2)
    res = ''
    for i in s:
        if i == ' ':
            continue
        else:
            res = res + i
    return res
str1 = input()
str2 = input()
print(func(str1,str2))
