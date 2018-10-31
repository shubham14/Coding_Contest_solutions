# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 01:00:13 2018

@author: Shubham
"""

import numpy as np

class Solution:
    def lszero(self, A):
        H = dict()
        max_diff = -1
        A_sum = np.cumsum(A)
        for ele in A_sum:
            H[ele] = [0,0,0]
       
        for i, ele in enumerate(A_sum):    
            if i == 0:
                H[ele] = [1, 0, 0]
            elif H[ele][0] == 1:
                if i > H[ele][2]:
                    H[ele][2] = i
            elif H[ele][0] == 0:
                H[ele] = [1, i, i]
                
        for k in list(H.keys()):
            if max_diff > H[k][2] - H[k][1]:
                max_diff = H[k][2] - H[k][1]
        return max_diff

if __name__ == "__main__":
    sol = Solution()
    a = sol.lszero([1,-2,2,-4,4])
    print(a)