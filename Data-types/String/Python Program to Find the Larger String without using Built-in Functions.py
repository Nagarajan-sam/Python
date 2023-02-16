def func(str1,str2):
    if len(str1) > len(str2):
        print('Larger string is:', str1)
    elif len(str1) < len(str2):
        print('Larger string is:', str2)
    else:
        print('Both are same length')
str1 = input()
str2 = input()
func(str1,str2)
