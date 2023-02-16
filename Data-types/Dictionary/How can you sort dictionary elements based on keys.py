import unittest
class TestLean(unittest.TestCase):
    def test_dic(self):
        d = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
        myKeys = list(d.keys())
        myKeys.sort()
        self.res = {}
        for i in myKeys:
            self.res.update({i:d[i]})
        print(self.res)
if __name__ ==  "__main__":
    unittest.main()
