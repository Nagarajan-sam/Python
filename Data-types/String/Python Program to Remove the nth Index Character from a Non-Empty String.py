str1 ='Msys India Tech Pvt Ltd'
def str2(n):
    res = ''
    for i in range(len(str1)):
        if i == n:
            continue
        else:
            res+=str1[i]
    return res
print(str2(6))
