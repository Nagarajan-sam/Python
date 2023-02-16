import unittest
class TestLearn(unittest.TestCase):
    def test_func(str1,str2):
        res=''
        for char in str1:
            if char in str2:
                continue
            else:
                res=res+char
        return res
    str1 = 'Msys'
    str2 = 'M'
    print(test_func(str1,str2))
if __name__ == "__main__":
    unittest.main()
