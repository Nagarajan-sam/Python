import unittest
class TestEvenodd(unittest.TestCase):
    def test_func(self):
        list1 = [4,10,5,5,9,6,7,8]
        temp = list(set(list1))
        self.res1 = []
        self.res2 = []
        for i in temp:
            if i % 2 == 0:
                self.res1.append(i)
            else:
                self.res2.append(i)
        print('Largest even number is:',self.res1[-1])
        print('Largest odd number is:',self.res2[-1])
if __name__ == "__main__":
    unittest.main()


