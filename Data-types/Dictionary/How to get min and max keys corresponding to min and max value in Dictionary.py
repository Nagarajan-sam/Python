import unittest
class TestKey(unittest.TestCase):
    def test_func(self):
        fruitsDict = {'Apple': 100,'Orange': 200,'Banana': 400,'pomegranate': 600}
        max_key = next(iter(fruitsDict))
        min_key = next(iter(fruitsDict))
        for key in fruitsDict:
            if fruitsDict[key] > fruitsDict[max_key]:
                max_key = key
        for key in fruitsDict:
            if fruitsDict[key] < fruitsDict[min_key]:
                min_key = key

        print('The max is',max_key)
        print('The min is',min_key)

if __name__ == "__main__":
    unittest.main()
