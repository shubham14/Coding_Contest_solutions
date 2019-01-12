# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 21:18:55 2019

@author: Shubham
"""

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.frequency = 0
        self.indexMinHeap = -1
        self.child = ['0'] * 26
        
class minHeapNode:
    