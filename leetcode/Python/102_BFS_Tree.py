# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 13:27:01 2018

@author: Shubham
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# solution containing the functions
# tuple storing the level and the node
class Solution:
    def levelOrder(self, root):
        queue = []
        final_print = []
        level = 1
        if root == None:
            return -1
        else:
            queue.insert(0, (level, root))
        while stack:
            level += 1
            if root.left:
                stack.insert(0, (level, root.left))
            if root.right:
                stack.insert(0, (level, root.right))
            stack.pop()
        
        max_level = stack[0][0]
        temp = []
        for i in range(len(stack)):
            if max_level == level:
                temp.append(stack[i][1])
            else:
                final_print.append(temp)
                temp = []
        
        return final_print
            
            