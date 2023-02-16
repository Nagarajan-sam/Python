import unittest
class TestLen(unittest.TestCase):
    def test_length(self):
        a=[1,2,3]
        self.res = len(a)
        if not a:
            return 0
        print(1 + len(a[1::2]) + len(a[2::2]))
if __name__ == "__main__":
    unittest.main()
