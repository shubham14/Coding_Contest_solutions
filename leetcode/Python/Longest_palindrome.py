# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 15:32:58 2018

@author: Shubham
"""

# formed in bottom-up manner
class Solution:
    def LongestPalim(self, str1):
        n = len(str1)
        table = [[0 for i in range(n)] for j in range(n)]
        # base case of length 1 and 2
        for i in range(n):
            table[i][i] = True
            maxLength = 1
        
        i = 0
        while i < n - 1:
            if str1[i] == str1[i + 1]:
                table[i][i + 1] = True
                start = i
                maxLength = 2
            i = i + 1
        
        # for palindrome of length 3 and above
        k = 3
        while k <= n:
            i = 0
            while i < n - k + 1:
                j = i + k - 1
                if table[i + 1][j - 1] and str1[i] == str1[j]:
                    table[i][j] = True
                    if k > maxLength:
                        maxLength = k
                i = i + 1
            k = k + 1
        
        return maxLength