def func(str1):
    digit=0
    letter=0
    for i in str1:
        if i.isdigit():
            digit+=1
        elif i.isalpha():
            letter+=1
    print('The total number digit present in a string is:',digit)
    print('The total number of letters present in a string is:',letter)
str1 = input()
func(str1)
