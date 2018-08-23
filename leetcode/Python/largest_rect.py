# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 20:58:12 2018

@author: Shubham
"""

class Solution(object):
    def maxAreaOfIsland(self, grid):
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for i in range(m)] for i in range(n)]
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and visited[r0][c0] != 1:
                    count = 0
                    stack = [(r0, c0)]
                    visited[r0][c0] = 1
                    while stack:
                        r, c = stack.pop()
                        count += 1
                        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                    and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans
    
if __name__ == "__main__":
    M = [[0,0,1,1,0],
         [1,0,1,1,0],
         [0,1,0,0,0],
         [0,0,0,0,1]]
    
    sol = Solution()
    ans = sol.largestRegion(M)
    print (ans)