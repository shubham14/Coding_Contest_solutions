# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 22:41:12 2018

@author: Shubham
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def zigzagLevelOrder(self, root):
        queue = []
        ans = []
        i = 0
        if root is None:
            return []
         else:
            queue.append(root)
            while len(queue) != 0:
                temp = queue.pop()
                ans.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            return ans
                
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
 
print ("Level order traversal of binary tree is -")
sol = Solution()

l = sol.zigzagLevelOrder(root)
print (l)        