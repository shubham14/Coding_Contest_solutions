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
        
class Path:
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
           
    def printPath(self, root):
        path = []
        self.printPathRec(root, path, 0)
        
    def printPathRec(self, root, path, pathlen):
        if root is None:
            return
        
        if(len(path) > pathlen):
            path[pathlen] = root.data
        else:
            path.append(root.data)
            
        pathlen += 1
        
        if root.left is None and root.right is None:
            for i in range(pathlen):
                print (path[i])
        else:
            self.printPathRec(root.left, path, pathlen)
            self.printPathRec(root.right, path, pathlen)
                
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.left.right = Node(5)
    root.left.left = Node(7)
    root.right = Node(9)
    p = Path()
    a = []
    a = p.rootpath(root, 10, a)
    print (a)
        