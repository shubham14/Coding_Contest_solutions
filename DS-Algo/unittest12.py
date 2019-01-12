# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:34:25 2019

@author: Shubham
"""

import unittest
import sys

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

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)
    
    def test1(self):
        print(quicksort(self.A, 0, len(self.A)-1))
        self.assertEqual(quicksort(self.A, 0, len(self.A)-1), sorted(self.A))
        
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        
if __name__ == "__main__":
    MyTest.A = [1,7,2,6,9,4]
    unittest.main()