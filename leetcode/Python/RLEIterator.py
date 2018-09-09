# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 15:37:58 2018

@author: Shubham
"""

import numpy as np

class RLEIterator:
    def __init__(self, A):
        self.RLE = []
        for i in range(0, len(A), 2):
            self.RLE += A[i] * [A[i + 1]]
        
    def next(self, n):
        # last element of the sliced array
        if n <= len(self.RLE):
            ans = self.RLE[:n][-1]
            self.RLE = self.RLE[n:]
        else:
            ans = -1
        return ans
        
if __name__ == "__main__":
    A = [3, 8, 0, 9, 2, 5]
    obj = RLEIterator(A)
    param_1 = obj.next(2)
    
    print("The list formed:")
    print(obj.RLE)
    
    print("The answer is :") 
    print(param_1)
    