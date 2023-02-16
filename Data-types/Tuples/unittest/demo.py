import unittest
class TestStringMethod(unittest.TestCase):
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        print("Statement executed successfully")`
if __name__ == "__main__":
    unittest.main()
