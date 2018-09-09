# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:42:24 2018
# tree and double linked list conversion
@author: Shubham
"""

# class DLL contains node intializations and helper functions to handle DLL
class DLL:
    def __init__(self, val):
        self.val = val
        self.head = None
        
        # pointers
        self.prev = None
        self.next = None

    def insert_DLL(self, val):
        temp = DLLNode(val)
        head_proxy = self.head
        while head_proxy:    
            head_proxy = head_proxy.next
        head_proxy.next = temp
        temp.prev = head_proxy
        return self.head
    
    def printDLL(self, head):
        temp = head
        while head:
            print (temp.val)
            tenp = temp.next

# node definitions
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        
class Tree_To_DLL:
    # inorder traversal for the tree
    def Inorder(self, root, res):
        if root is not None:
            res = self.Inorder(root.left, res)
            res.append(root.val)
            res = self.Inorder(root.right, res)
        return res
    
    def convert(self, root):
        if root is not None:
            res = self.Inorder(root)
            res = res[::-1]
            root_DLL = DllNode(res[0])
            
            
            # covering edge case where the tree has only one node
            if len(res) >= 1:
                for i in range(1, len(res)):
                    root_DLL.insert(res[i])
        return root_DLL
    
                    
                    
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2);
    root.right = TreeNode(3);
    root.left.left  = TreeNode(4);
    root.left.right = TreeNode(7);
    root.right.left = TreeNode(10);
    
    sol = Tree_To_DLL()
    res = []
    res = sol.Inorder(root, res)
    print (res)