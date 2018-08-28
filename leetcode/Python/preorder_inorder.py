# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 23:20:42 2018

@author: Shubham
"""

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right= None
        
class Solution:
    # search function
    def search(self, arr, inst, inend, data):
        for i, ele in enumerate(arr):
            if ele == data:
                return i
        return -1
    
    # new Node function
    def newNode(self, x):
        temp = Node(x)
        return temp
    
    # construct Tree
    # check for invalidity to be added earlier
    def constructTree(self, inOrder, preOrder, instart, inend):
        start_ind = 0
        temp = self.newNode(preOrder[start_ind])
        start_ind += 1
        
        if instart == inend:
            return temp
        
        ind = self.search(inOrder, instart, inend, temp.val)
        temp.left = self.constructTree(inOrder, preOrder, instart, ind - 1)
        temp.right = self.constructTree(inOrder, preOrder, ind + 1, inend)
        
        return temp
    
    def printInorder(self, root):
        if root is None:
            return ;
        printInorder(root.left)
        print (root.val)
        printInorder(root.right)