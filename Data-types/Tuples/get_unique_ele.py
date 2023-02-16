def func(val):
        res = []
        s = set()
        for i in val:
                for j in i:
                        if not j in s:
                                s.add(j)
                                res.append(j)
 
        print("Unique Element in Nested Tuples : " ,res)
val = [(1, 3, 5), (4, 5, 7), (1, 2, 6), (10, 9), (10,)]
func(val)
