# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:35:30 2018

@author: Shubham
"""

import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FdgO')
    
    
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'woPld'])
        with self.assertRaises(TypeError):
            s.split(2)
            
if __name__ == "__main__":
    unittest.main()