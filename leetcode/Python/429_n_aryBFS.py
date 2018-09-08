# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 17:06:26 2018

@author: Shubham
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.children = [] 
        
class Solution:
    def N_Ary_BFS(self, root):
        q, ret = [root], []
        while any(q):
            ret.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]
        return ret
    
if __name__ == "__main__":
    root = Node(10)
    root.children.append(Node(2))
    root.children.append(Node(34))
    root.children.append(Node(56))
    root.children.append(Node(100))
    root.children[2].children.append(Node(1))
    root.children[3].children.append(Node(7))
    root.children[3].children.append(Node(8))
    root.children[3].children.append(Node(9))
    
    sol = Solution()
    ret = sol.N_Ary_BFS(root)
    print(ret)