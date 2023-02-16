import unittest
class TestSum(unittest.TestCase):
    def test_func(self):
        d = {'a': 100, 'b':200, 'c':300}
        res = 0
        for i in d.values():
            res = res + i
        print(res)
if __name__ == "__main__":
    unittest.main()
