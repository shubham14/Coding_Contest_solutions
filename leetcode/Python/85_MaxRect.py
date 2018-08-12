# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 14:33:14 2018

@author: Shubham
"""

import numpy as np
import math

class Solution(object):
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
    
    def maximalRectangle(self, matrix):
        ans = list(map(lambda x: int(x), matrix[0]))
        maxArea = self.maxHistArea(ans)
        if len(matrix) != 1:
            for i in range(1, len(matrix)):
                temp = list(map(lambda x, y: x + int(y), ans, matrix[i]))
                maxArea = max(maxArea, self.maxHistArea(temp))
        return maxArea