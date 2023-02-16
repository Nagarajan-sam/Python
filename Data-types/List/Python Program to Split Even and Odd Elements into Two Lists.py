import unittest
class TestSplit(unittest.TestCase):
    def test_func(self):
        list1 = [4,10,5,5,9,6,7,8]
        self.res1 = []
        self.res2 = []
        for i in list1:
            if i % 2 == 0:
                self.res1.append(i)
            else:
                self.res2.append(i)
        print(self.res1)
        print(self.res2)
if __name__ == "__main__":
    unittest.main()
