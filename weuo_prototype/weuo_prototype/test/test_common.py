'''
Created on 2012-9-29

@author: weuo
'''
import unittest
from weuo_prototype.common import Utilities


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_common(self):
        _utility = Utilities(x = 1, y =2)
        self.assertEqual(1, _utility.get_x(), 'first test')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_common']
    unittest.main()