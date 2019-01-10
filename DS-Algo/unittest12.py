# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:34:25 2019

@author: Shubham
"""

import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)
    
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        
    def test_isupper(self):
        self.assertFalse('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        
if __name__ == "__main__":
    unittest.main()