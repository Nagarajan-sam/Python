import unittest
class TestLearn(unittest.TestCase):
    def test_empd(self):
        emp = {'Jack': 12000, 'Max': 20000, 'Hack': 25000, 'Nack': 80000}
        self.res = {}
        for key,value in emp:
            if (int(value) < 20000):
                self.res.update({key:value})
        print(self.res)
if __name__ == "__main__":
    unittest.main()
