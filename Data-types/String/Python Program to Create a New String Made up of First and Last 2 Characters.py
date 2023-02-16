def func(str1):
    res=''
    for i in range(0,len(str1)):
        if i == 0 or i == (len(str1)-1):
            res+=str1[i]
    return res
str1 = input()
print(func(str1))
