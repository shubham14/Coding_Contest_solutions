# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:44:55 2019

@author: Shubham
"""

from collections import deque

def minSlidingwindow(A, k):
    n = len(A)
    ans = []
    Qi = deque()
    for i in range(k):
        while Qi and A[i] <= A[Qi[-1]]:
            Qi.pop()
        Qi.append(i)
    
    for i in range(k, n):
        ans.append(A[Qi[0]])
        while Qi and Qi[0] <= i-k:
            Qi.popleft()
        while Qi and A[i] <= A[Qi[-1]]:
            Qi.pop()
        Qi.append(i)
    ans.append(A[Qi[0]])
    return ans

def rotateMatrix(A):
    N = len(A)
    for i in range(N//2):
        for j in range(N-1-i):
            temp = A[i][j]
            A[i][j] = A[N-1-j][i]
            A[N-1-j][i] = A[N-i-1][N-1-j]
            A[N-1-i][N-1-j] = A[j][N-1-i]
            A[j][N-i-1] = temp

def intersectionWords(str1, str2, wordList):
    str1 = set(str1.split())
    str2 = set(str2.split())
    wordList = set(wordList.split())
    a = str1 - wordList
    b = str2 - wordList
    return a == b

if __name__ == "__main__":
    A = [1, 2, 4, 5, 6, 3, 2, 4, 6, 8]
    k = 3
    ans = minSlidingwindow(A, k)
    print(ans)
    
    mat = [[1,2,3], [4,6,3], [2,5,1]]
    rotateMatrix(mat)