# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 19:54:35 2018

@author: Shubham
"""

import numpy as np

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # M is numpy array
    def pad_array(self, M):
        a,b = M.shape
        M_new = np.zeros((a+2, b+2))
        for i in range(1, a+1):
            for j in range(1, b+1):
                M_new[i][j] = M[i-1][j-1]
        return M_new
        
    def imageSmoother(self, M):
        M_np = np.array(M)
        a, b = M_np.shape
        res = np.ones((a, b))
        res1 = self.convolution2d(M_np, res)
        return res1
    
    def convolution2d(self, image, kernel):
        m, n = kernel.shape
        if (m == n):
            y, x = image.shape
            y = y - m + 1
            x = x - m + 1
            new_image = np.zeros((y,x))
            for i in range(y):
                for j in range(x):
                    new_image[i][j] = np.sum(image[i:i+m, j:j+m]*kernel)
        return new_image
    
    def DFS(self, root, stack):
        if root:
            stack = self.DFS(root.left, stack)
            stack.append(root.val)
            stack = self.DFS(root.right, stack)
        return stack
    
    def sec_min(self, root):
        st = self.DFS(root, [])
        st = list(set(st))
        st.sort()
        if len(st) > 1:
            return st[1]
        else:
            return -1
    
if __name__ == "__main__":
    sol = Solution()
    root = Node(1) 
    root.left      = Node(2) 
    root.right     = Node(3) 
    root.left.left  = Node(4) 
    root.left.right  = Node(5) 
    