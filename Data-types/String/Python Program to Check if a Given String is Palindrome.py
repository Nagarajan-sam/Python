def func(str):
    res = ''
    for i in str:
        res = i + res
    if res == str:
        print('The given string is palindrome')
    else:
        print('The given string is not a palindrome')

str = input("Enter a string: ")
func(str)
