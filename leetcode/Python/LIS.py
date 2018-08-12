# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 01:41:08 2018

@author: Shubham
"""

class Solution:
    def Least_Inc_Sub(self, l):
        LIS = []
        
        # base base
        if len(l) == 0:
            return 0
        
        # forming an auxiliary LIS array
        for i in range(len(l)):
            LIS.append(1)
            
        for i in range(len(l)):
            for j in range(i):
                if l[i] > l[j] and LIS[i] < LIS[j] + 1:
                    LIS[i] = LIS[j] + 1
                
        ans = max(LIS) # return the maximum value from the LIS array
        
        return ans
    
if __name__ == "__main__":
    l = [10, 22, 9, 33, 21, 50, 41, 60]
    sol = Solution()
    ans = sol.Least_Inc_Sub(l)
    print(ans)