def func(tuple1,tuple2):
    tuple3 = tuple1
    tuple1 = tuple2
    tuple2 = tuple3
    print(tuple1)
    print(tuple2)
tuple1 = (1,2)
tuple2 = (3,4)
func(tuple1,tuple2)
