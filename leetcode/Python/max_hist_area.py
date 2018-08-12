# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 15:09:44 2018

@author: Shubham
"""

import numpy as np

class Solution:
    def maxHistArea(self, hist):
        stack, maxArea, i  = [], 0, 0
        while i <= len(hist):
            if not stack or (i < len(hist) and hist[i] > hist[stack[-1]]):
                stack.append(i)
                i += 1
                
            else:
                last = stack.pop()
                if not stack:
                    maxArea = max(maxArea, hist[last] * i)
                else:
                    maxArea = max(maxArea, hist[last] * (i - stack[-1] - 1))
        return maxArea
            
    
if __name__ == "__main__":
    sol = Solution()
    print (sol.maxHistArea([2,1,5,6,2,3]))