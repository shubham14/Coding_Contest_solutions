# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 17:59:23 2018

@author: Shubham
"""

import numpy as np

class Solution:
    def thirdMax(self, nums):
        v = [float('-inf')] * 3
        if len(nums) <= 2:
            return max(nums)
        for num in nums:
            if num > v[0]:
                v = [num, v[0], v[1]]
            elif num > v[1]:
                v = [v[0], num, v[1]]
            elif num > v[2]:
                v = [v[0], v[1], num]
        if v[2] == -float('inf'):return v[0]
        return v[2]
    
