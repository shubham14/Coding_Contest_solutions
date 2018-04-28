# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 11:39:26 2018

@author: Shubham
"""

class Solution:
    
    def numComponents(self, head, G):
        count = 1
        temp = head
        while temp.next != None:
            if temp.val in G:
                continue
            else:
                count = count + 1
            temp = temp.next
        return count