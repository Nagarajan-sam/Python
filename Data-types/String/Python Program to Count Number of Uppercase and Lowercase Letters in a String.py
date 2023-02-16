def func(str1):
    upper = 0
    lower = 0
    for i in str1:
        if ('A'<=i<='Z'):
            upper+=1
        elif ('a'<=i<='z'):
            lower+=1
    print('The total number of uppercase is:',upper)
    print('The total number of lowercase is:',lower)
str1 = input()
func(str1)
