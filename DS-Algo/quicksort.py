# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 14:27:20 2018

@author: Shubham
"""

import numpy as np

def Quicksort(A, start, end):

    if (start < end):
        p = Partition(A, start, end)
        Quicksort(A, start, p-1)
        Quicksort(A, p+1, end)
        
def Partition(A, start, end):
    i = start - 1
    pivot = A[end]
    for j in range(start, end):
        if A[j] < pivot:
            i += 1
            
            # swapping elements 
            A[i], A[j] = A[j], A[i]
    A[end], A[i+1] = A[i+1], A[end]
    return (i+1)


A = [1,5,3,8,9,6]
Quicksort(A, 0, len(A)-1)
print (A)