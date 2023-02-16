import unittest
class TestLst(unittest.TestCase):
    def test_func(self):
        s = ['Smith', 'John', 'Priska', 'Abhi']
        m = [89, 53, 92, 86]
        students_dict = dict(zip(s,m))
        print(students_dict)
if __name__ == "__main__":
    unittest.main()
