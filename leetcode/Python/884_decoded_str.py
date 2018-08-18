# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 19:42:57 2018

@author: Shubham
"""

import math

class Solution:
    def maxArea(self, A, B, C, D, E, F, G, H):
        areaSum = (C-A)*(D-B) + (G-E)*(H-F)
        if(E>=C or A>=G or B>=H or F>=D):
            return areaSum
        bX = max(A, E)
        bY = max(B, F)
        tX = min(C, G)
        tY = min(D, H)
        areaIntersect = (tX-bX)*(tY-bY);
        return areaSum - areaIntersect
    
    def minSquare(self, n):
        s = [i*i for i in range(1, int(math.sqrt(n)) + 1)]
        l = 0
        currentLevel = [0]
        
        while True:
            nextLevel = []
            for a in currentLevel:
                for b in s:
                    if a + b == n:
                        return l + 1
                    if a + b < n:
                        nextLevel.append(a + b)
            currentLevel = list(set(nextLevel))
            l += 1
            
    def rev_str(self, str1, st, end):
        while st <= end:
            str1[st], str1[end] = str1[end], str1[st]
            st += 1
            end -= 1
        return str1
    
    def rev_sent(self, sent):
        start = 0
        end = 0
        sent = list(sent)
        for i, ele in enumerate(sent):
            if ele == ' ' and start != end:
                end = i - 1
                sent = self.rev_str(sent, start, end)
                start = i + 1
        sent = self.rev_str(sent, start, len(sent)-1)
        return sent
    
class MinStack:
    def __init__(self):
        self.min_stack = []
        self.top = -1
        self.minEle = 1000000
        self.next_minEle = 999999
        
    def push(self, x):
        self.min_stack.append(x)
        self.top += 1
        if x < self.minEle:
            self.next_minEle = self.minEle
            self.minEle = x
        
        
    def pop(self):
        if self.min_stack[self.top] == self.minEle:
            self.minEle = self.next_minEle
        self.min_stack.pop()
        self.top -= 1
        
    def top(self):
        return self.min_stack[self.top]
    
    def getMin(self):
        return self.minEle