import unittest
class TestSum(unittest.TestCase):
    def test_sum(self):
        list1 = [1,2,3,4]
        size = len(list1)
        self.total = sum(list1, len(list1))
        if (size == 0):
            return 0
        else:
            print(list1[size - 1] + sum(list1, size - 1))

        print("Sum of all elements in given list: ", self.total)
if __name__ == "__main__":
    unittest.main()
