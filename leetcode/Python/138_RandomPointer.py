# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 00:02:43 2018

@author: Shubham
"""

from collections import defaultdict

class Node:
    def __init__(self, x):
        self.x = x
        self.next = None
        self.random_next = None
        
class Solution:
    def __init__(self, visitedHash):
        self.visitedHash = visitedHash
    
    def copy_List(self, head):
        if head == None:
            return None
        
        head_copy = head
        
        # maintaining a visited list for each node
        visited = defaultdict(Node)
        
        if head in self.visitedHash:
            return self.visitedHash[head]
        
        node = Node(head.x)
        
        self.visitedHash[head] = node
        
        node.next = self.copy_List(head.next)
        node.random = self.copy_List(head.random)
        
        return node
        
            