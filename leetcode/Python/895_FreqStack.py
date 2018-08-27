# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 19:54:09 2018

@author: Shubham
"""

from collections import defaultdict
import operator

# MOD is for a hashing key
class FreqStack:
    def __init__(self, MOD):
        self.hashMap = defaultdict(int)
        self.stack = []
        self.MOD = MOD
    
    def push(self, x):
        self.hashMap[x] += 1
        self.stack.append(str(x))
        
    def pop(self):
        highest = max(self.hashMap.values())
        l = ([k for k, v in count.items() if v == highest])
        return self.stack[max(l)]
        