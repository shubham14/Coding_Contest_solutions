# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 00:13:39 2018

@author: Shubham
"""

from collections import defaultdict 
import numpy as np
import math

class RandomizedSet:
    
    def __init__(self):
        self.s = []
        self.hashmap = defualtdict(int)
    
    def insert(self, val):
        if self.hashmap[val] == 0:
            self.s.append(val)
            self.hashmap[val] = 1
            return True
        elif self.hashmap[val] == 1:
            return False
        
    def remove(self, val):
        try:
            ans = l.index(val)
            self.s.remove(ans)
            return True
        except:
            ans = -1
            return False

    def getRandom(self):
        l = len(self.s)
        x = math.floor(np.random.uniform(l))
        return self.s[x]