def func(str1):
    res=''
    for i in range(0,len(str1)):
        if i == 0:
            res = res + str1[len(str1)-1]
        elif i == (len(str1)-1):
            res = res + str1[0]
        else:
            res = res + str1[i]
        
    return res
str1 = input()
print(func(str1))
