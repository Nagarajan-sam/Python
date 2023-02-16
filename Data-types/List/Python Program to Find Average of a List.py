import unittest
class TestAverage(unittest.TestCase):
    def test_func(self):
        lst = [4, 5, 1, 2, 9, 7, 10, 8]
        self.res = 0
        for i in lst:
            self.res = self.res + i
        temp = self.res/len(lst)
        print(temp)
if __name__ == "__main__":
    unittest.main()
