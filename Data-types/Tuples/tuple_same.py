def func(tup):
        lst=list(tup)
        res = lst[0]
        chk = True
        for item in lst: 
                if res != item:
                    chk = False
                    break
         
        if (chk == True):
            print("All items in the tuple are the same")
        else:
            print("All items in the tuple are the not same")
tup = (10,10,10,10)
func(tup)
