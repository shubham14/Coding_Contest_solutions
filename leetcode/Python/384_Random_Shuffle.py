# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 14:43:23 2018

@author: Shubham
"""
import numpy as np

class Solution:
    
    def __init__(self, nums):
        self.nums = nums
        self.original = list(nums)
        
    def reset(self):
        return self.original
    
    def shuffle(self):
        aux = list(self.nums)

        for idx in range(len(self.nums)):
            remove_idx = random.randrange(len(aux))
            self.nums[idx] = aux.pop(remove_idx)

        return self.nums
        
    
if __name__ =="__main__":
    obj = Solution(nums)
    param1 = obj.reset()
    param2 = obj.shuffle()