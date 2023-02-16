def func(lst):
    res = []
    for i in lst:
        res = res + [(i, i**2)]
    return res
lst = [1, 2, 3]
print(func(lst))
