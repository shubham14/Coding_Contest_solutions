# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 23:52:25 2019

@author: Shubham
"""

class Solution:
    def minWindow(self, s, t):
        n, counter = len(s), len(t)
        begin, end, head = 0, 0, 0
        min_len = n + 1
        dic = dict()
        
        # hash table to store charecter count
        for ch in t:
            dic[ch] = dic.get(ch, 0) + 1
        
        while end < n:
            if s[end] in dic:
                if dic[s[end]] > 0:
                    counter -= 1
                dic[s[end]] -= 1
            
            end += 1
            
            # counter == 0 means all charecters in substring 
            # are covered
            while counter == 0:
                if end - begin < min_len:
                    min_len = end - begin
                    head = begin
                
                if s[begin] in dic:
                    dic[s[begin]] += 1
                    if dic[s[begin]] > 0:
                        counter += 1
                begin += 1
        
        if min_len == n+1:
            return ""
        return s[head: head+min_len]
    
        
        