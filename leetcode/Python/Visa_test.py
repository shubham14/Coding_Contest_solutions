# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 11:20:17 2018

@author: Shubham
"""


def numberOfPairs(a, k): 
    s = set() 
    ans = []
    for i in range(len(a)): 
        temp = k-a[i] 
        if (temp>=0 and temp in s): 
            ans.append((a[i], temp)) 
        s.add(a[i])
    ans = list(set(list(map(lambda x: tuple(sorted(x)), ans))))
    return len(ans), ans

def numberOfWays(n):
    # Write your code here
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    dp = dict()
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    for i in range(4, (n+1)):
        if i < 10 ** 6:
            dp[i] = (dp[i-1] + dp[i-3]) % (10**9 + 7)
        elif i % 10 ** 6 == 0:
            dp[i % 10 ** 6] = (dp[(i-1) % 10 **6] + dp[(i-3) % 10 ** 6]) % (10**9 + 7)
        elif i > 10 ** 6:
            dp[i % 10 ** 6] = (dp[(i-1) % 10 **6] + dp[(i-3) % 10 ** 6]) % (10**9 + 7)
    return dp[n%10**6]
#    
def algo(a, b):
    x = a 
    y = b
    while x != y:
        if x > y:
            x = x - y
        elif x < y:
            y = y - x
    return x