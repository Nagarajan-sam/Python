import unittest
class TestNes(unittest.TestCase):
    def test_func(self):
        people = {1: {'name': 'kohli', 'age': '35', 'profession': 'cricketer',"lastname":"virat"},2: {'name': 'rohit', 'age': '37', 'profession': 'cricketer',"lastname":"sharma"}}
        people[3] = {}
        people[3]['name'] = 'raina'
        people[3]['age'] = '37'
        people[3]['profession'] = 'cricketer'
        people[3]['lastname'] = 'suresh'
        print(people)
if __name__ == "__main__":
    unittest.main()
