import unittest
class TestEmpty(unittest.TestCase):
    def test_func(self):
        m = {'lang': 'C#', 'Fruit': 'Apple', 'Subj': None, 'Animal': None}
        for value in m.items():
            if value is None:
                del m[key]
        print(m)
if __name__ == "__main__":
    unittest.main()
