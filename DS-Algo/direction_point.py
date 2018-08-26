# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 20:33:48 2018

@author: Shubham
"""

# point class definition
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        
class Solution:
    # A, B, C are point members
    def direction(self, A, B, C):
        B.x -= A.x
        B.y -= A.y
        C.x -= A.x
        C.y -= A.y
        
        # cross product definition
        cross_prod = B.x * C.y - B.y * C.x
        
        if cross_prod > 0:
            direc = "RIGHT"
        elif cross_prod < 0:
            direc = "LEFT"
        else:
            direc = "COLLINEAR"
        return direc
            
if __name__ == "__main__":
    # point instantiating
    A = Point(2,3)
    B = Point(-1,5)
    C = Point(0,-3)
    
    sol = Solution()
    ans = sol.direction(B, A, C)
    print (ans)