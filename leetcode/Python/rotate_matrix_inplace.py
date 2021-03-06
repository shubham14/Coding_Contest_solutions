# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 20:34:16 2018

@author: Shubham
"""

import numpy as np
import sys

class Solution:
    
    def rotateMatrix(self, mat):
        N = len(mat)
        for x in range(0, int(N/2)):
            for y in range(x, N-x-1):
                temp = mat[N-1-y][x] 
                mat[N-1-y][x] = mat[N-1-x][N-1-y] 
                mat[N-1-x][N-1-y] = mat[y][N-1-x]
                mat[y][N-1-x] = mat[x][y]
                mat[x][y] = temp 
                
     
    def display(self, mat):
        N = len(mat)
        for i in range(0, N):
            for j in range(0, N):
                print (mat[i][j], end = ' ')
            print ("")
     
     
if __name__ == "__main__": 
    sol = Solution()
    mat = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
    mat1 = mat
    sol.rotateMatrix(mat)
    sol.display(mat)