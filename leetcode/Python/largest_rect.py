# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 18:44:28 2018
Max area of islands
@author: Shubham
"""

class Solution:
    def __init__(self, A):
        self.A = A
        self.visited = [[0 for i in range(len(self.A[0]))] 
                    for j in range(len(self.A))]
        
    def dfs(self, r, c):
        if 0 <= r < len(A) and 0 <= c < len(A[0]):
            if self.A[r][c] and not self.visited[r][c]:
                self.visited[r][c] = 1
                return (1 + self.dfs(r + 1, c) + self.dfs(r - 1, c) +
                    self.dfs(r, c - 1) + self.dfs(r, c + 1))
        return 0
        
    def maxArea(self):
        return max(self.dfs(i, j) for i in range(len(self.A))
                   for j in range(len(self.A[0])))        
        
if __name__ == "__main__":
    A = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    sol = Solution(A)
    ans = sol.maxArea()
    print (ans)