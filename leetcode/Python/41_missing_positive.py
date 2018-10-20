# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 18:40:01 2018

@author: Shubham
"""

import numpy as np

class Solution:
    def firstMissingPositive(self, nums):
        min_nums = 1000000
        max_nums = -1000000
        s = sum(nums)
        for i in range(len(nums)):
            if nums[i] > max_nums:
                max_nums = nums[i]
            if nums[i] < min_nums:
                min_nums = nums[i]
        
        if max_nums <= 0 :
            return 1
        elif min_nums >= 0:
            sumtotal = ((max_nums - min_nums) * (max_nums + min_nums + 1)) / 2
            print (sumtotal)
            t = sumtotal - s
            if t == 0:
                return max_nums + 1
            else:
                return t
        else:
            sumneg =  - (abs(min_nums) * (abs(min_nums) + 1)) / 2
            sumpos = (abs(max_nums) * (abs(max_nums) + 1)) / 2
            return sumneg + sumpos - s
        
if __name__ == "__main__":
    inp = [7,8,9,11,12]
    sol = Solution()
    ans = sol.firstMissingPositive(inp)
    print (ans)