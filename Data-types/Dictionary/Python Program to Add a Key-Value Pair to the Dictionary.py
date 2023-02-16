import  unittest
class TestVal(unittest.TestCase):
    def test_func(self):
        key= int(input())
        value= int(input())
        self.d={}
        self.d.update({key:value})
        print(self.d)
if __name__ == "__main__":
    unittest.main()
    

