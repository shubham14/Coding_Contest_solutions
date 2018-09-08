# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 15:15:53 2018

@author: Shubham
"""

import numpy as np

class Solution:
    def __init__(self, n):
        self.A = [i for i in range(1, n+1)]
        
    def lastRemaining(self):
        count = 1
        count *= 2
        self.A = list(filter(lambda x: x%count == 0, self.A))
        odd_round = False
        while len(self.A) != 1:
            count *= 2
            if self.A[len(self.A) - 1] % count == 2 and odd_round == False:
                self.A = list(filter(lambda x: x%count == 0, self.A))
            elif self.A[len(self.A) - 1] % count == 2 and odd_round == True:
                self.A = list(filter(lambda x: x%count == 2,self. A))
            elif self.A[len(self.A) - 1] % count == 0 and odd_round == False:
                self.A = list(filter(lambda x: x%count == 2, self.A))
            else:
                self.A = list(filter(lambda x: x%count == 0, self.A))
        return self.A[len(self.A)-1]