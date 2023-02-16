def func(str,substr):
    if substr in str:
        print('Substring present in a given string')
    else:
        print('Substring not present in a given string')
str = input()
substr = input()
func(str,substr)
