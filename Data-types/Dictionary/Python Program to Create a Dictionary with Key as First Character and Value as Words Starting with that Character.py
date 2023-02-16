import unittest
class TestChar(unittest.TestCase):
    def test_func(self):
        str1 = input("Enter a string: ")
        words = str1.split()
        dic = {}
        for word in words:
            if (word[0].lower() not in dic.keys()):
                dic[word[0].lower()] = []
                dic[word[0].lower()].append(word)
  
            else:
                if (word not in dic[word[0].lower()]):
                    dic[word[0].lower()].append(word)
  
        print(dic)
if __name__ == "__main__":
    unittest.main()

