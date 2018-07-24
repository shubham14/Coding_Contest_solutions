# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 22:37:32 2018

@author: Shubham
"""

import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution(object):
    def leafnodes(self, root1):
        if root == None:
            return []
        elif root1.right == None and root1.left == None:
            return [root1.val]
        else:
            return self.leafnodes(root1.right) + self.leafnodes(root1.left)
        
    def leafSimilar(self, root1, root2):
        l1 = self.leafnodes(root1)
        l2 = self.leafnodes(root2)
        compare = lambda x,y : x == y
        return compare(l1, l2)
    
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    
    sol = Solution()
    sameLeaves = sol.leafSimilar(root, root1)
    print (sameLeaves)