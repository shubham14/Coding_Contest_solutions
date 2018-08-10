# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 10:59:29 2018

@author: Shubham
"""

# sort Anagrams grouped together

import numpy as np

class Solution:
    def sortAnagrams(self, l):
        l1 = list(map(lambda x: ''.join(sorted(x)), l))
        # sorting the words in the list and storing the indices
        r = np.argsort(l1)
        T = [l[i] for i in r]
        return T
    
if __name__ == "__main__":
    l = ['bac','test','vac', 'abc', 'london', 'cba', 'cav', 'lon', 'pst']
    sol = Solution()
    ans = sol.sortAnagrams(l)
    print (ans)