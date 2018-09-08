# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 15:15:53 2018

@author: Shubham
"""

import numpy as np

class Solution:
    def lastRemaining(self, n):
        A = [i for i in range(1, n+1)]
        count = 1
        count *= 2
        A = list(filter(lambda x: x%count == 0, A))
        odd_round = False
        while len(A) != 1:
            count *= 2
            if A[len(A) - 1] % count == 2 and odd_round == False:
                A = list(filter(lambda x: x%count == 0, A))
            elif A[len(A) - 1] % count == 2 and odd_round == True:
                A = list(filter(lambda x: x%count == 2, A))
            elif A[len(A) - 1] % count == 0 and odd_round == False:
                A = list(filter(lambda x: x%count == 2, A))
            else:
                A = list(filter(lambda x: x%count == 0, A))
        return A[len(A)-1]
        
                