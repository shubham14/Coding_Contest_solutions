# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:08:43 2019

@author: Shubham
"""


class Node:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.val = val
        self.key = key
        
class LRUCache:
    def __init__(self, capacity : 'int'):
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    
    def get(self, key : 'int') -> 'int':
        if key in self.d:
            node = self.d[key]
            self._del(node)
            self._add(node)
            return node.val
        return node
    
    def put(self, key : 'int', val : 'int') -> None:
        if key in self.d:
            node = self.d[key]
            self._del(node)
            node.val = val
            self._add(node)
            self.d[key] = node
        else:
            node = Node(key, val)
            self.d[key] = node
            self._add(node)
            if len(self.d) > self.capacity:
                self.d.pop(self.head.next.val)
                self._del(self.head.next)
                
    def _add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        
    def _del(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev