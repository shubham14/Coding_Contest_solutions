# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 23:32:48 2018

@author: Shubham
"""

# bottom up DP formulation
class Solution:
    def isMatch(self, s, p):
        n = len(s)
        m = len(p)
        if n == 0:
            return m == 0
        
        dp = [[False] * (m+1)] * (n+1)
        dp[0][0] = True
        
        for j in range(1, m+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or (s[i-1] == s[i-2])
                elif p[j-1] == '.' or p[j-1] == s[i -1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = False
        return dp[n][m]
    
if __name__ == "__main__":
    p = "c*a*b"
    s = "aab"
    sol = Solution()
    d = sol.isMatch(s, p)
    print(d)