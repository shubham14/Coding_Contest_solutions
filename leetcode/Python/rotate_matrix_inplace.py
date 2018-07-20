# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 20:34:16 2018

@author: Shubham
"""

import numpy as np
import sys

class Solution:
    
    def __init__(self, A):
        self.A = A
    
    def rotate(self):
        N = len(self.A)
        for i in range(int(N/2)):
            for j in range(N-i-1):
                temp = self.A[i][j]
                self.A[i][j] = self.A[j][N-1-i]
                self.A[j][N-1-i] = self.A[N-i-1][N-j-1]
                self.A[N-i-1][N-j-1] = self.A[N-j-1][i]
                self.A[N-j-1][i] = temp
        return self.A
                
    def display(self, B):
        N = len(B)
        for i in range(N):
            for j in range(N):
                print (B[i][j], end=' ')
            print("")
                
if __name__ == "__main__":
    N = 5
    mat = [[x+y for x in range(N)] for y in range(N)]
    sol = Solution(mat)
    mat = sol.rotate()
    sol.display(mat)