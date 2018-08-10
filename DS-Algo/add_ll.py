# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 11:32:31 2018

@author: Shubham
"""

import math

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    root = n = ListNode(0)
    carry = 0
    def addTwoNumbers(self, l1, l2):
        if l1 == None and l2 == None:
            return None
        else:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry = (v1 + v2 + carry) % 10
            val_node = (v1 + v2 + carry) / 10
            n.next = ListNode(val_node)
            n = n.next
        return root.next