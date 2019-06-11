#our unit test
import unittest
from activities import eat, nap, is_funny, laugh 

class ActivityTests(unittest.TestCase):
    'tests for functins eat and nap from activities.py'
    def test_eat_healthy(self):
        """Testing eat_heathy"""
        self.assertEqual(
                eat("brocoli", is_healthy=True),
                "I'm eating brocoli, because I am Broly"
            )
    def test_eat_unhealthy(self):
        """Testing eat_unhealthy"""
        self.assertEqual(
                eat("pizza", is_healthy=False),
                "I'm eating pizza, because I'm in my feelings"
            )
    def test_eat_healthy_boolean(self):
        """Testing it be a boolean and not a string"""
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy = "string here, should be boolean")
    
    def test_nap_short(self):
        """Testing sleep for 1"""
        self.assertEqual(nap(1),"I slept for 1 hour!")
    def test_nap_long(self):
        """Testing sleep for 3"""
        self.assertEqual(nap(3),"I slept for 3 hours!")
    def test_is_funny(self):
        """Should return person is funny: True"""
        self.assertFalse(is_funny("Donald"),False)
    def test_is_funny_anyone_else(self):
        """every one is funny except Donald"""
        self.assertTrue(is_funny("Jon"),"True, he super funny")
        self.assertTrue(is_funny("Kim"), "She funny and cute")
    def test_laugh(self):
        """Should be the following laughs"""
        self.assertIn(laugh(),("haha","lol","bwahaha"))
        


if __name__ == "__main__":
    unittest.main()