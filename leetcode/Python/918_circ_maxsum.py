# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 19:58:39 2018

@author: Shubham
"""

import numpy as np

class Solution:
    def maxSubarraySumCircular(self, A):
        B = A + [A[0]]
        max_so_far = 0
        curr_max = 0
        for i in range(len(B)):
            curr_max = max(0, curr_max + B[i])
            max_so_far = max(curr_max, max_so_far)
        return max_so_far
    
if __name__ == "__main__":
    sol = Solution()
    l = [5, -3, 5]
    ans = sol.maxSubarraySumCircular(l)
    print (ans)