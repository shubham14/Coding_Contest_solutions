# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 10:42:41 2018

@author: Shubham
"""

import numpy as np

class Solution:
    
    def edit_dist(self, str1, str2):
        m = len(str1)
        n = len(str2)
        # create a DP array
        DP = [[0 for x in range(n + 1)] for y in range(m + 1)]
        
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    DP[i][j] = j
                
                elif j == 0:
                    DP[i][j] = i
                
                elif str1[i - 1] == str2[j - 1]:
                    DP[i][j] = DP[i-1][j-1]
                    
                else:
                    DP[i][j] = 1 + min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1])
        
        return DP[m][n]
        
    
    # str1 is the base string and l is the list of strings
    def char_edit_check(self, str1, l):
        
        # list contains the lengths of each string
        len_l = list(map(lambda x: self.edit_dist(str1, x), l))
        ans = []
        for i, ele in enumerate(len_l):
            if len_l[i] == 1:
                ans.append(l[i])
                
        return ans
    
if __name__ == "__main__":
    str1 = "apple"
    l = ["apps", "pineapple", "apples"]
    sol = Solution()
    ans = sol.char_edit_check(str1, l)
    print(ans)