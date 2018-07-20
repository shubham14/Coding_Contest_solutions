# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 22:34:01 2018

@author: Shubham
"""

from collections import defaultdict

A = [1, 4, 5, 7, 9]
d = defaultdict(int)
ans = []
k = 2
for i in range(len(A)):
    A.sort()
    if d[A[i]] == 0:
        d[A[i]] = 1
        d[A[i] + k] = 1
        if A[i] + k in A:
            ans.append((A[i], A[i] + k))
    elif d[A[i]] == 1:
        if A[i] + k in A:
            ans.append((A[i], A[i] + k))
        
    ans = set(ans)
    ans = list(ans)

print (ans)