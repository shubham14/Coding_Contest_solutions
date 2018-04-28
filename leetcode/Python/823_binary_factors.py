# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 10:02:19 2018

@author: Shubham
"""

class Solution(object):
    
    def countSubTrees(self, A):
        t = {}
        for a in sorted(A):
            t[a] = 1 + sum(t[b] * t.get(a/b, 0) for b in A if b < a)
        return sum(t.values()) % (10**9 + 7) 
        
if __name__ == "__main__":
    
    l = [2, 4]
    sol = Solution()
    ans = sol.countSubTrees(l)
    print (ans)
        
            