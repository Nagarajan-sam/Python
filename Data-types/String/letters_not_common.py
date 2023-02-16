import unittest
class TestLearn(unittest.TestCase):
    def test_func(str1, str2):
        for char in str1:
            if char not in str2:
                print(char)
    str1 = input()
    str2 = input()
    test_func(str1, str2)
if __name__ == "__main__":
    unittest.main()
