# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 15:40:59 2018

@author: Shubham
"""

import collections
import operator

class Solution:
    def frequencySort(self, str1):
        ans = ''
        c = dict(collections.Counter(str1))
        x = sorted(c.items(), key=operator.itemgetter(1))
        x.reverse()
        x = dict(x)
        for k in x:
            ans += k*x[k]
        return ans
    
    
if __name__ == "__main__":
    sol = Solution()
    str1 = "Tree"
    a = sol.frequencySort(str1)
    print(a)