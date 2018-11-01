# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 02:32:59 2018

@author: Shubham
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def reverse(self, st, end):
        curr = st
        prev = None
        while curr != end:
            next_n = curr.next
            curr.next = prev
            prev = curr
            curr = next_n
        st = next_n
        
    def reverseList(self, A, B):
        temp = A
        while temp is not None:
            st = temp; 
            for i in range(B):
                temp = temp.next
            end = temp
            self.reverseList(st, end)
            temp = temp.next
        return A
    
    def printList(self, A):
        t = A
        while t is not None:
            print (t.val)
            t = t.next
            
if __name__ == "__main__":
    