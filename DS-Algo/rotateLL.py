# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 13:22:50 2019

@author: Shubham
"""

import numpy as np

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def convertLL(self, head):
        if head is None:
            return None
        temp = head1 = head
        while temp.next is not None:
            temp = temp.next
        temp.next = head
        head = temp
        return head
    
    def shiftCLL(self, head, k):
        c = 0
        temp = head
        while c < k:
            temp = temp.next
            c += 1
        head = temp
        t = head
        while t.next != head:
            t = t.next
        t.next = None
        return head
            
    
    def printCList(self, head):
        temp = head
        while temp.next != head:
            print(temp.val)
            temp = temp.next
        print(temp.val)
        
    def printLList(self, head):
        temp = head
        while temp.next is not None:
            print(temp.val)
            temp = temp.next
        print(temp.val)
        
if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(4)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)
    head.next.next.next.next = ListNode(10)
    
    s = Solution()
    h1 = s.convertLL(head)
    s.printCList(h1)
    print('-------------')
    h2 = s.shiftCLL(h1, 2)
    s.printLList(h2)