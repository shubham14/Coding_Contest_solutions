# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 17:01:25 2018

@author: Shubham
"""

import numpy as np

class Solution:
    def dominantIndex(self, nums):
        nums.sort()
        ind = len(nums) - 1
        ans = -1
        while ind >= 0:
            if nums[ind - 1] != 0:
                if nums[ind] / nums[ind - 1] >= 2:
                    ans = max(ans, nums.index(nums[ind]))
            ind = ind - 1
        return ans