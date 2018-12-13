# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 12:57:10 2018

@author: Shubham
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def addTwoLists(self, first, second):
        prev = None
        temp = None
        carry = 0
        
        while first is not None or second is not None:
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data
            carry = 1 if Sum >= 10 else 0
            Sum = Sum if Sum < 10 else Sum % 10
            temp = Node(Sum)
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp
            
            prev = temp
            if first in not None:
                first = first.next
            if second is not None:
                second = second.next
            
        if carry > 0:
            temp.next = Node(carry)
            
    def printList(self):
        h = self.head
        while(h):
            print (h.data)
            h = h.next
        