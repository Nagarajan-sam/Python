def func(str1):
    s = str1.split()
    counts = {}
    words = str1.split()
    for i in words:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    for key in counts:
        print(key, ":", counts[key])
str1 = input()
func(str1)
