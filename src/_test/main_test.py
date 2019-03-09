import unittest
import sys
sys.path.append("..")
from main import greeting 

class TestCase01(unittest.TestCase):
    # test function MUST start with test_
    def test_greeting(self):
         result = greeting("world")
         self.assertEqual(result, "hello world")

if __name__ == '__main__':
     unittest.main()

