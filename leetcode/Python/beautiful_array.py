# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 11:37:39 2018

@author: Shubham
"""

from collections import deque
import numpy as np

class Solution:
    def beautifulArray(self, N):
        arr = [i for i in range(1, N+1)]
        for i in range(0, len(arr), 2):
            if i < len(arr)-1:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        return arr
    
    def minDepth(self, root):
        if not root:
            return 0
        else:
            node_deque = deque([(1, root)])
        
        # Adopted BFS approach
        while node_deque:
            depth, root = node_deque.popleft()
            children = [root.left, root.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    node_deque.append((depth+1, c))
    
    def hammingPair(self, a, b):
        c = a ^ b
        ans = 0
        while c:
            ans += c & 1
            c = c >> 1
        return ans
    
    def totalHammingDistance(self, nums):
        if len(nums) <= 1:
            return 0
        ans = 0
        m = max(nums)
        n = len(nums)
        while m:
            s = list(map(lambda x: x & 1, nums))
            s1 = sum(s)
            s2 = n - s1
            if s1 != n and s2 != n:
                ans += s1*s2
            nums = list(map(lambda x: x>>1, nums))
            m = max(nums)
        return ans
    
    def isSafe(self, A, m, n, i, j):
            return i >= 0 and i < m and j >=0 and j < n
    
    def reachRow(self, A):
        children = [(0, -1), (1, -1), (1, 0),
                    (1, 1), (0, 1), (-1, 1),
                    (-1, 0), (-1, -1)]
        m, n = A.shape
        visited = np.zeros((m, n))
        root = []
        for i in range(n):
            if A[0][i] == 1:
                root.append((i, 0))
        
        
        while root:
            tmp_i = root[0][0]
            tmp_j = root[0][1]
            stack = []
            stack.append((tmp_i, tmp_j))
            while stack:
                top = stack.pop()
                if visited[top[0]][top[1]] != 1:
                    visited[top[0]][top[1]] = 1
                if top[0] == m-1:
                    return True
                for ele in children:
                    if self.isSafe(A, m, n, tmp_i + ele[0], tmp_j + ele[1]) and visited[tmp_i + ele[0]][tmp_j + ele[1]] != 1:
                        stack.append((tmp_i + ele[0], tmp_j + ele[1]))
                          
            root.pop(0)
        return False
    
    def array_print(self, A, n):
        m = len(A)
        if n > m:
            print (A)
            return 
        for i in range(1, n+1):
            ans = []
            for j in range(m-i+1):
                B = A[j:j+i]    
                ans.append(B)
            print (ans)
            
            
    
if __name__ == "__main__":
    sol = Solution()
    ans = sol.beautifulArray(5)
    print (ans)