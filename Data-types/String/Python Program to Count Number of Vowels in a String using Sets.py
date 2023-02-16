def func(str1):
    count=0
    v = set('AEIOUaeiou')
    for i in str1:
        if i in v:
            count+=1
    return count
str1 = input()
func(str1)
