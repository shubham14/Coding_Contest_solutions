# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:34:25 2019

@author: Shubham
"""

import unittest
import sys
import os

def fun(x):
    return x + 1

def partition(A, low, high):
    i = low - 1
    x = A[high]
    for j in range(low, high):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[high] = A[high], A[i+1]
    return i+1
    

def quicksort(A, low, high):
    if low < high:
        pi = partition(A, low, high)
        quicksort(A, low, pi-1)
        quicksort(A, pi+1, high)
    return A


class CustomAssertions:
    def assertFileExists(self, path):
        if not os.path.lexists(path):
            raise AssertionError('File not exists in path "' + path + '".')

class MyTest(unittest.TestCase, CustomAssertions):
        
    def test(self):
        self.assertEqual(fun(3), 4)
    
    def test1(self):
        print(quicksort(self.A, 0, len(self.A)-1))
        self.assertEqual(quicksort(self.A, 0, len(self.A)-1), sorted(self.A))
        
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)


def suite():
    tests = ['test_default_size', 'test_resize']
    return unittest.TestSuite(map(MyTest, tests))

def suite1():
    suite = unittest.TestSuite()
    suite.addTest(MyTest('test1'))
    suite.addTest(MyTest('test_upper'))
    return suite
        
if __name__ == "__main__":
#    MyTest.A = [1,2,3,4,32,2,2,3,4,5,8,4,0]
#    unittest.main()
   
#    suite3 = unittest.TestLoader().loadTestsFromTestCase(MyTest)

    widgetTestSuite = unittest.TestSuite()
    widgetTestSuite.addTest(MyTest('test_split'))
    runner = unittest.TextTestResult()
    runner.run(widgetTestSuite())
    