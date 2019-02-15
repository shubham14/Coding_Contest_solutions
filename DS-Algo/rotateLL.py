# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 13:22:50 2019

@author: Shubham
"""

import numpy as np

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def convertLL(self, head):
        if head is None:
            return None
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = head
        head = temp
        return head
    
    def shiftCLL(self, head, k):
        c = 0
        temp = head
        while c < k:
            temp = temp.next
            c += 1
        head = temp
        t = head
        while t.next != head:
            t = t.next
        t.next = None
        return head
            
    
    def printCList(self, head):
        temp = head
        while temp.next != head:
            print(temp.val)
            temp = temp.next
        print(temp.val)
        
    def printLList(self, head):
        temp = head
        while temp.next is not None:
            print(temp.val)
            temp = temp.next
        print(temp.val)
        
        
def evalString(A, B, op):
    if op == '+':
        return int(ord(A) - ord('0')) + int(ord(B) - ord('0'))
    elif op == '-':
        return int(ord(A) - ord('0')) - int(ord(B) - ord('0'))
    elif op == '*':
        return int(ord(A) - ord('0')) * int(ord(B) - ord('0'))
    else:
        return int(ord(A) - ord('0')) / int(ord(B) - ord('0'))
        
def evaluateExpression(string):
    operator_stack = []
    operand_stack = []
    priority = {'+':2, '-':1, '*':3, '/':4}
    for i, c in enumerate(string):
        if c in ['+', '-', '*', '/']:
            if len(operand_stack) > 1 and len(operator_stack) >= 1:
                if priority[c] >= priority[operator_stack[-1]] and i < len(string)-1:
                    operator_stack.append(c)
                elif priority[c] > priority[operator_stack[-1]] and i == len(string)-1:
                    A = operand_stack.pop()
                    B = operand_stack.pop()
                    C = operator_stack.pop()
                    res = str(evalString(A, B, C))
                    operand_stack.append(res)
                elif priority[c] < priority[operator_stack[-1]] and i < len(string)-1:
                    A = operand_stack.pop()
                    B = operand_stack.pop()
                    C = operator_stack.pop()
                    res = str(evalString(A, B, C))
                    operand_stack.append(res)
                    operator_stack.append(res)       
        elif c not in ['+', '-', '*', '/']:
            operand_stack.append(c)
            
    return operand_stack
                
        
if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(4)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)
    head.next.next.next.next = ListNode(10)
    
    s = Solution()
    h1 = s.convertLL(head)
    s.printCList(h1)
    print('-------------')
    h2 = s.shiftCLL(h1, 2)
    s.printLList(h2)