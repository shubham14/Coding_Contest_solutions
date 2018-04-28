# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 00:22:41 2018

@author: Shubham
"""

import re
import math

class Solution:
    
    def shortestToChar(self, S, C):
        # list to store the result
        ans = []
        
        # regex for finding the indices to the charecter in the string
        ind = [x.start() for x in re.finditer(C, S)]
        for i, char in enumerate(S):
            c = 0
            # traverse the index list till you find the bucket where the index belongs
            while i > ind[c]:
                c = c + 1
                
            # base cases of first and last occurances of the charecter
            if c == 0:
                ans.append(abs(ind[c] - i))
            elif c == len(ind) - 1:
                ans.append(min(abs(ind[c] - i),abs(ind[c - 1] - i)))
            else:
                ans.append(min(abs(ind[c] - i), abs(ind[c + 1] - i)))
        return ans
    
if __name__ == "__main__":
    
    sol = Solution()
    S = "loveleetcode"
    C = 'e'
    print (sol.shortestToChar(S, C))