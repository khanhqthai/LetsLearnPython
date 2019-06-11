import unittest

from robot import Robot

class RobotTests(unittest.TestCase):
    
    #create initial data we will use to in our tests
    #setUp is ran every time before a test function, insure the initial data is always the same
    def setUp(self):
        self.mega_man = Robot("Mega Man", battery=50)
        
    def test_charge(self):
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery, 100)
    
    def test_say_name(self):
        self.assertEqual(self.mega_man.say_name(), "BEEP BOOP BEEP BOOP. I AM MEGA MAN")
        self.assertEqual(self.mega_man.battery, 49)
    def test_learn_skill(self):
        ''
    
    def tearDown(self):
        'this fucntion is ran by unit test after each test case'
if __name__ == "__main__":
    unittest.main()