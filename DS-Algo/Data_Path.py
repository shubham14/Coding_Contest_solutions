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
           
    def printPath(self, root, s):
        path = []
        a = self.printPathRec(root, s, path, 0)
        return a
        
    def printPathRec(self, root, s, path, pathlen):
        if root is None:
            return []
        
        if(len(path) > pathlen):
            path[pathlen] = root.data
        else:
            path.append(root.data)
            
        pathlen += 1
        
        if s == 0:
            return path
        else:
            if root.left:
                self.printPathRec(root.left, s-root.left.data, path, pathlen)
            if root.right:
                self.printPathRec(root.right, s-root.right.data, path, pathlen)
                
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.left.right = Node(5)
    root.left.left = Node(7)
    root.right = Node(9)
    p = Path()
    a = p.printPath(root, 10)