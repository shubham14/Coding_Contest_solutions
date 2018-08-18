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
                return True
            elif l[start] + l[end] < sum1:
                start += 1
            else:
                end -= 1
        return False
    
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left) 
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res
    
    def twoSumTree(self, root, sum1):
        res = self.inorderTraversal(root)
        print (res)
        ans = self.twoSum1(res, sum1)
        return ans
            
    
if __name__ == "__main__":
    l =  ['bac','test','vac', 'abc', 'london', 'cba', 'cav', 'lon', 'pst']
    root = Node(1)
    root.left      = Node(2)
    root.right     = Node(3)
    root.left.left  = Node(4)
    root.left.right  = Node(5)
    sol = Solution()
    l1 = [2, 7, 11, 15]
    sum1 = 13

    ans = sol.sortAnagrams(l)
    ans1 = sol.twoSum1(l1, sum1)
    ans2 = sol.twoSumTree(root, 9)

    print(ans)
    print(ans1)