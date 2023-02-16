def func(str1):
    v = 'aeiouAEIOU'
    count = 0
    for i in str1:
        if i in v:
            count+=1
    return count
str1 = input()
print(func(str1))
