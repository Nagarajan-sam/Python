import unittest
class TestNeg(unittest.TestCase):
    def test_func(self):
        lst = [2,5,7,3,6,-3,-2]
        self.n = 0
        self.pe = 0
        self.po = 0
        for i in lst:
            if i < 0:
                self.n+=i
            elif i % 2 == 0:
                self.pe+=i
            else:
                self.po+=i
        print('Sum of negative number is:', self.n)
        print('Sum of positive even number is:', self.pe)
        print('Sum of positive odd number is:',self.po)
if __name__ == "__main__":
    unittest.main()
