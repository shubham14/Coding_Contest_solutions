# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 15:50:24 2018

@author: Shubham
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
def sol(nums):
    j = 0
    n = len(nums)
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
    for k in range(j, n):
        nums[k] = 0
    
    return nums
