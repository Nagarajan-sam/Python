import unittest
class TestCpy(unittest.TestCase):
    def test_func(self):
        original = {1: 'geeks', 2: 'for'}
        new = original.copy()
        print('new: ', new)
        print('original: ', original)
if __name__ == "__main__":
    unittest.main()
