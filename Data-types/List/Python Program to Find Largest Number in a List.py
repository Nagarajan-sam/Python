import unittest
class TestLarge(unittest.TestCase):
    def test_func(self):
        lst = [4,5,9,6,7,8]
        temp = lst[0]
        for i in lst:
            if temp < i:
                temp = i
        print(temp)
if __name__ == "__main__":
    unittest.main()
    

