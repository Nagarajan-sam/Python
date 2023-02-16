def func(str1):
    res=1
    res1=0
    for i in str1:
        res1+=1
        if (i == ' '):
            res+=1
    print('The number of words is:', res)
    print('The number of characters is:', res1)
str1 = input()
func(str1)
