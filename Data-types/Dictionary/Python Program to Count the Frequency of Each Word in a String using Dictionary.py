import unittest
class TestCount(unittest.TestCase):
    def test_func(self):
        str1 =input("Enter a string: ")
        str2 = str1.split()        
        str3 = []
        for i in str1:
            if i not in str3:
                str3.append(i)
        for i in range(0, len(str3)):
            print('Frequency of', str3[i], 'is :', str1.count(str3[i]))
if __name__ == "__main__":
    unittest.main()
