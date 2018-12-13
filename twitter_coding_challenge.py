# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 20:40:20 2018

@author: Shubham
"""

import threading
import time

def roverMove(matrixSize, cmds):
    n = matrixSize
    left_count = 0
    right_count = 0
    up_count = 0
    down_count = 0
    for ele in cmds:
        if ele == 'LEFT':
            left_count += 1
        elif ele == 'RIGHT':
            right_count += 1
        elif ele == 'UP':
            up_count += 1
        else:
            down_count += 1
    add_x = 0
    if right_count - left_count < 0:
        add_x = 0
    elif right_count - left_count > n-1:
        add_x = n-1
    else:
        add_x = right_count - left_count
        
    if down_count - up_count < 0:
        add_y = 0
    elif down_count - up_count > n-1:
        add_y = n-1
    else:
        add_y = down_count - up_count
        
    return add_y * n + add_x 
        
def f(n, l=[]):
    for i in range(n):
        l.append(i*i)
    print(l)
    
def loop1_10():
    for i in range(1, 11):
        time.sleep(1)
        print (i)
        
threading.Thread(target=loop1_10).start()

class node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value
   
def inorder(root):
    if root:
        inorder(root.left)
        if root.val == '+':
            return left_sum + right_sum
        
        elif root.val == '-':
            return left_sum - right_sum
    
        elif root.val == '*':
            return left_sum * right_sum
    
        elif root.val == '/':
            return left_sum / right_sum
        inorder(root.right)
     
def evaluateExpressionTree(root):
    if root is None:
        return 0
    
    if root.left is None and root in None:
        return int(root.val)
    
    left_sum = evaluateExpressionTree(root.left)
    right_sum = evaluateExpressionTree(root.right)
    
    if root.val == '+':
        return left_sum + right_sum
        
    elif root.val == '-':
        return left_sum - right_sum
    
    elif root.val == '*':
        return left_sum * right_sum
    
    elif root.val == '/':
        return left_sum / right_sum
      
if __name__=='__main__': 
      
    # creating a sample tree 
    root = node('+') 
    root.left = node('*') 
    root.left.left = node('5') 
    root.left.right = node('4') 
    root.right = node('-') 
    root.right.left = node('100') 
    root.right.right = node('20') 
    (inorder(root))