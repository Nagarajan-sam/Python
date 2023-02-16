import unittest
class TestMul(unittest.TestCase):
    def test_func(self):
        d = {'a': 1, 'b':2, 'c':3}
        res = 1
        for i in d.values():
            res = res * i
        print(res)
if __name__ == "__main__":
    unittest.main()
