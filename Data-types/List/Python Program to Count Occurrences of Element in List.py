import unittest
class TestCount(unittest.TestCase):
    def test_func(self):
        num1 = [1, 2, 3, 4, 5, 3, 2, 3, 4]
        n = 2
        self.count = 0
        for i in num1:
            if i == n:
                self.count+=1
        print(n, "is present" ,self.count, "times in a list")

if __name__ == "__main__":
    unittest.main()
