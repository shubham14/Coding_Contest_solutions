# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 13:59:11 2018

@author: Shubham
"""

class Solution:
    def maxSlidingWindow(self, nums, k):
        max_ans = []
        max_ans.append(max(nums[:k]))
        if k == 1:
            return nums
        if len(nums) == 0:
            return 0
        for i in range(0, len(nums)):
            if i + k <= len(nums):
                window = nums[i: i+k]
                max_ans.append(max(window))
        return max_ans
    
if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    sol = Solution()
    ans = sol.maxSlidingWindow(nums, k)
    print(ans)