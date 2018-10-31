# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 19:36:41 2018

@author: Shubham
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
class LCA:
    def findLCA(self, root, n1, n2):
        if root is None:
            return None
        
        # one of the nodes is the root
        if root.key == n1 or root.key == n2:
            return root
        
        left_lca = self.findLCA(root.left, n1, n2)
        right_lca = self.findLCA(root.right, n1, n2)
        
        if left_lca and right_lca:
            return root
        return left_lca if left_lca is not None else right_lca