def func(tuple1):
    count=0
    for i in tuple1:
        if i == 10:
            count+=1
    return count
tuple1 = (50, 10, 60, 70, 10)
print(func(tuple1))
