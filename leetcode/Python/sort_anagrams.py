# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 23:15:00 2018

@author: Shubham
"""

import numpy as np
from collections import defaultdict

class Solution:
    def sortAnagrams(self, list_str):
        d = defaultdict(list)
        for ele in list_str:
            d[''.join(sorted(set(ele)))].append(ele)
        
        keys = sorted(d.keys())
        ans = []
        for ele in keys:
            d[ele].sort()
            ans.append(d[ele])
            
        return ans
    
    def twoSum(self, l, sum1):
        d = defaultdict(int)
        for ele in l:
            if d[sum1-ele] == 1:
                return True
            else:
                d[ele] = 1
                d[sum1-ele] = 1
        return False
    
    def twoSum1(self, l, sum1):
        start = 0
        end = len(l)-1
        while start <= end:
            if l[start] + l[end] == sum1:
                return start+1, end+1
            elif l[start] + l[end] < sum1:
                start += 1
            else:
                end -= 1
        return -1, -1
            
    
if __name__ == "__main__":
    l =  ['bac','test','vac', 'abc', 'london', 'cba', 'cav', 'lon', 'pst']
    sol = Solution()
    l1 = [2, 7, 11, 15]
    sum1 = 13
    ans = sol.sortAnagrams(l)
    ans1 = sol.twoSum1(l1, sum1)
    print(ans)
    print(ans1)