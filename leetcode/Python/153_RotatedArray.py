# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 15:38:52 2018

@author: Shubham
"""

import numpy as np

class Solution:
    # tester function for rotate
    # clockwise to be true, rotation in a clockwise manner
    def rotate(self, A, k, clockwise):
        l = len(A)
        A_2 = A + A
        if clockwise:
            res = A_2[l - k : 2*l - k]
        else:
            res = A_2[k: l + k]
        return res
    
    # rotation array minimum element
    def minRotateArray(self, A, low, high):
        if high < low:
            return A[0]
        
        if high == low:
            return A[low]
        
        mid = int(low + (high - low)/2)
        
        if mid < high and A[mid] > A[mid + 1]:
            return A[mid]
        
        if A[high] > A[mid]:
            return self.minRotateArray(A, low, mid - 1)
        return self.minRotateArray(A, mid + 1, high)
        
if __name__ == "__main__":
    A = [3,4,5,1,2]
    sol = Solution()
    ans = sol.minRotateArray(A, 0, len(A)-1)
    print (ans)
    