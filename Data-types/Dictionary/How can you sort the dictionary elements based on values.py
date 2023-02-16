import unittest
class TestDic(unittest.TestCase):
    def test_func(self):
        d = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
        myvalues = list(d.values())
        myvalues.sort()
        self.res = {}
        for i in myvalues:
            for k in d.keys():
                if d[k] == i:
                    self.res[k] = d[k]
 
        print(self.res)
if __name__ == "__main__":
    unittest.main()
