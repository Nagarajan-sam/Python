import unittest
class TestClr(unittest.TestCase):
    def test_func(self):
        d = {1: "geeks", 2: "for"}
        d.clear()
        print(d)
if __name__ == "__main__":
    unittest.main()
