# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 00:09:31 2018

@author: Shubham
"""

class Solution(object):
    def minEatingSpeed(self, piles, H):
        def possible(K):
            return sum((p - 1)/ K + 1 for p in piles) <= H
        
        s, e = 1, max(piles)
        while s < e:
            m = (s + e)/2
            if not possible(m):
                s = m + 1
            else:
                e = m
        return s
    
