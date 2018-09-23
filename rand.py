# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 15:09:43 2018

@author: Shubham
"""

# longest common substring
import numpy as np
import pandas as pd
from collections import defaultdict

class Solution:
    def LCS(self, a, b):
        m = len(a); n = len(b)
        DP = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    DP[i][j] = 0
                elif a[i-1] == b[j-1]:
                    DP[i][j] = 1 + DP[i-1][j-1]
                else:
                    DP[i][j] = max(DP[i-1][j], DP[i][j-1])
        return DP[m][n]
    
    def maxSubArraySum(self, A):
        curr_sum = A[0]
        max_so_far = A[0]
        for i in range(len(A)):
            curr_sum= max(curr_sum, curr_sum + A[i])
            max_so_far = max(curr_sum, max_so_far)
        return max_so_far
    
    # here A is a 2D matrix
    # where all elements are positive
    def kadane2D(self, A):
        col = len(A)
        row = len(A[0])
        maxSum = -1
        for i in range(0, col):
            temp = []
            for j in range(i, col):
                sum1 = 0
                for z in range(row):
                    sum1 += M[i][j]
                
            
        
    
if __name__ == "__main__":
    str1 = "AGGTAB"; 
    str2 = "GXTXAYB";
    sol = Solution()
    ans = sol.LCS(str1, str2)
    print (ans)