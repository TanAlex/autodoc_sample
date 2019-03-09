import unittest
import sys
sys.path.append("..")
from utils import  *
from time import sleep

class TestCase01(unittest.TestCase):
    # test function MUST start with test_
    def test_progressbar(self):
         # A List of Items
        items = list(range(0, 57))
        l = len(items)

        # Initial call to print 0% progress
        printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
        for i, item in enumerate(items):
            # Do stuff...
            sleep(0.1)
            # Update Progress Bar
            printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)


if __name__ == '__main__':
     unittest.main()
