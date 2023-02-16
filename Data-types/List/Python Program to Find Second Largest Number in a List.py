import unittest
class TestSlarge(unittest.TestCase):
    def test_func(self):
        list1 = [4,10,5,5,9,6,7,8]
        res = list(set(list1))
        print('Second largest number is:',res[-2])
if __name__ == "__main__":
    unittest.main()
