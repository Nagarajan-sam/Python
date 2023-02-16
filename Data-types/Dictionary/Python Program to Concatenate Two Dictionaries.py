import unittest
class TestCon(unittest.TestCase):
    def test_func(self):
        d1={'A':1,'B':2}
        d2={'C':3,'D':4}
        d1.update(d2)
        print(d1)
if __name__ == "__main__":
    unittest.main()
