# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 10:02:19 2018

@author: Shubham
"""

class Solution(object):
    
    def __init__(self, l):
        self.l = l
    
    # function to search a number in sorted array in O(logn)
    def binarySearch(self, num, start, end):
        
        # sorting the array for binary search
        self.l.sort()
        mid = int((start + end)/2)
        print (self.l)
        # recursion for binary search
        if (self.l[mid] == num):
            return 1
        if self.l[mid] > num:
            return self.binarySearch(num, start, mid - 1)
        if self.l[mid] < num:
            return self.binarySearch(num, mid + 1, end)
        if num > l[end]:
            return -1
        return -1
    
    def countSubTrees(self):
        ans = len(self.l)
        for i in range(len(l)):
            for j in range(len(l)):
                # parameters for the binary search
                start = 0
                end = len(self.l) - 1
                num = i*j
                search = self.binarySearch(num, start, end)
                if (search == 1):
                    if (i == j):
                        # for the case where square of the number is to be found
                        ans = ans + 1
                    else:
                        # for symmetric cases, for example 10 2 5 and 10 5 2
                        ans = ans + 2
            return ans
        
if __name__ == "__main__":
    
    l = [2, 4]
    sol = Solution(l)
    ans = sol.countSubTrees()
    print (ans)
        
            