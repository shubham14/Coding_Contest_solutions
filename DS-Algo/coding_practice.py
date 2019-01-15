# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 17:10:32 2019

@author: Shubham
"""

def interleavingStrings(str1, str2, str3):
    '''
    str1 and str2 are the input strings
    str3 is the resultant strings
    '''
    m = len(str1); n = len(str2)
    DP = [[0 * len(n) + 1] * len(m) + 1]
    
    if m + n != len(str3):
        return False
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                DP[i][j] = True
            if j == 0 and str1[i-1] == str3[i-1]:
                DP[i][j] = DP[i-1][j]
            if i == 0 and str2[j-1] == str3[j-1]:
                DP[i][j] = DP[i][j-1]
            else:
                if str1[i] == str3[i+j-1] and str2[j] != str3[i+j-1]:
                    DP[i][j] = DP[i-1][j]
                if str1[i] != str3[i+j-1] and str2[j] == str3[i+j-1]:
                    DP[i][j] = DP[i][j-1]
                if str1[i-1] == str3[i+j-1] and str2[j] == str3[i+j-1]:
                    DP[i][j] == DP[i-1][j] or DP[i][j-1]
    return DP[m][n]

class Solution:
    def binarySearch(self, A, l, r, x):
        if l > r:
            mid = int((r - l)/2 + l)
            if x > A[mid]:
                return (mid-1, mid)
            else:
                return (mid-1, mid)
        else:
            mid = int((r - l)/2 + l)
            if x == A[mid]:
                return (mid, mid)
            elif x > A[mid]:
                return self.binarySearch(A, mid+1, r, x)
            else:
                return self.binarySearch(A, l, mid-1, x)
            
    def findClosestElements(self, arr, k, x):
        ans = []
        n = len(arr)
        l,r = self.binarySearch(arr, 0, n-1, x)
        if l == -1:
            l = 0
        if r == n:
            r = n-1
        c = 0
        while c < k:
            print (l, r)
            if x - arr[l] >= arr[r] - x:
                ans.append(arr[l])
                l -= 1
                c += 1
            elif x - arr[l] < arr[r] - x:
                ans.append(arr[r])
                r += 1
                c += 1
            elif l < 0:
                r += 1
                c += 1
            elif r > n-1:
                l -= 1
                c += 1
            else:
                c += 1
        return ans
    
    def kClosest(self, points, K):
        l = list(map(lambda x: x[0]**2 + x[1]**2, points))
        d = dict(zip(points, l))
        sorted_by_value = sorted(d.items(), key=lambda kv: kv[1])
        k = sorted_by_value.keys()[:K]
        return k
