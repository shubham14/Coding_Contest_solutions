# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 19:42:13 2018

@author: Shubham
"""

from collections import Counter

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def inorder(self, root, ans):
        if root:
            ans = self.inorder(root.left, ans)
            ans.append(root.val)
            ans = self.inorder(root.right, ans)
        return ans
    
    def BSTmode(self, root):
        ans = []
        ans = self.inorder(root, [])
        c = Counter(ans).most_common()[0]
        return c
        
    
if __name__ == "__main__":
    root = TreeNode(1) 
    root.left = TreeNode(2) 
    root.right = TreeNode(3) 
    root.left.left = TreeNode(4) 
    root.left.right = TreeNode(5) 
      
    sol = Solution()
    ans = []
    ans = sol.inorder(root, ans) 
    m = sol.BSTmode(root)
    print (m)