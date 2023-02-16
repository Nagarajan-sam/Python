import unittest
class TestRmv(unittest.TestCase):
    def test_func(self):
        d = {'a':1,'b':2,'c':3,'d':4}
        print('Before deleting:',d)
        del d['b']
        print('After deleting:',d)
if __name__ == "__main__":
    unittest.main()
