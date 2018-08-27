# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 15:16:33 2018

@author: Shubham
"""

# solution in O(n) time complexiety and O(1) space complexiety

class Solution:
    def findDuplicate(self, nums):
        for i in range(len(nums)):
            if nums[abs(nums[i])] < 0:
                return nums[i]
            else:
                nums[abs(nums[i])] *= -1
                