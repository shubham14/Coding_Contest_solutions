# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 23:52:51 2018

@author: Shubham
"""
class Solution:
    def anagrams(self, t):
        t = list(t)
        t = list(map(lambda x: ''.join(sorted(x)), t))
        d = dict()
        ans = []
        for i, ele in enumerate(t):
            if ele not in d.keys():
                d[ele] = [i+1]
            else:
                d[ele].append(i+1)
        for k in d.keys():
            ans.append(d[k])
        return ans