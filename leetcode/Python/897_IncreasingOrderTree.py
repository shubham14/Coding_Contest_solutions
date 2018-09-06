# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 16:10:30 2018

@author: Shubham
"""

import numpy as np

class TreeNode:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
        
class IncTree:
    # helper functions for inoder traversal
    def inorder(self, root, lis):
        if root:
            self.inorder(root.left, lis)
            lis.append(root.data)
            self.inorder(root.right, lis)
        return lis
    
    def orient(self, root):
        l = []
        l = self.inorder(root, l)
        rootNew = TreeNode(l[0])
        for i in range(1, len(l)):
            rootNew.right = TreeNode(l[i])
            rootNew = rootNew.right
        return rootNew
    