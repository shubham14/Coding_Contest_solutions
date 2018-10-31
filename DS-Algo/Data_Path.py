# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 22:10:58 2018

@author: Shubham
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
class path:
    def rootpath(self, root, sum1, ans):
        if root == None:
            ans = [] 
            return ans
        elif sum1 == 0:
            ans.append(root.data)
        else:
            if root.left:
                ans.append(root.left.data)
                ans = (self.rootpath(root.left, sum1-root.left.data, ans))
            if root.right:
                ans.append(root.right.data)
                ans = (self.rootpath(root.right, sum1-root.right.data, ans))
                
                

        
        