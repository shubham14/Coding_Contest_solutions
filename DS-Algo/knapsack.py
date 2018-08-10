# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 22:48:46 2018

@author: Shubham
"""

# DP implentation of knapsack problem
def knapsack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],
                             K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][w]

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapsack(W, wt, val, n))

def mySupPow(a, b):
    flag = True
    ans = a
    if b == 0:
        return 1.0
    elif b == 1:
        return a % 1337
    while(flag):
        if b % 2 == 0:
            ans = ans * ans 
            b = b / 2
        else:
            ans *= a
            b -= 1
        if b == 0:
            flag = False
    return ans

print (mySupPow(2, 10))