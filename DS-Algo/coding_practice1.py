# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 20:30:19 2019

@author: Shubham
"""

import numpy as np

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class RandomNode:
    def __init__(self, label):
        self.label = label
        self.next = None
        self.random = None

class Solution:
    def __init__(self):
        self.visitedHash = {}
    
    def copyRandomList(self, head):
        if head == None:
            return None
        
        if head in self.visitedHash:
            return self.visitedHash[head]
        
        node = RandomNode(head.data)
        self.visitedHash[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node

def reverse(head):
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
    return head

def push(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    head = new_node
    return head

def printList(head):
    temp = head
    while(temp):
        print (temp.data)
        temp = temp.next
        

def reverseBetween(head, m, n):
    if not head:
        return None

    # Move the two pointers until they reach the proper starting point
    # in the list.
    cur, prev = head, None
    while m > 1:
        prev = cur
        cur = cur.next
        m, n = m - 1, n - 1

    # The two pointers that will fix the final connections.
    tail, con = cur, prev

    # Iteratively reverse the nodes until n becomes 0.
    while n:
        third = cur.next
        cur.next = prev
        prev = cur
        cur = third
        n -= 1

    # Adjust the final connections as explained in the algorithm
    if con:
        con.next = prev
    else:
        head = prev
    tail.next = cur
    return head

def reverseSecondHalf(head):
    c = 1
    fast = slow = head
    while fast.next.next is not None and slow.next is not None:
        fast = fast.next.next
        c += 1
        slow = slow.next
    head1 = reverseBetween(head, c+1, 2*c)
    printList(head1)

head = Node(1)
head = push(head, 2)
head = push(head, 5)
head = push(head, 3)
head = push(head, 7)
head = push(head, 9)

print ('--- Original List ---')
printList(head)
#
print ('--- Reversed List ---')
h = reverseSecondHalf(head)
printList(h)

class Queue:
    def __init__(self):
        self.stack = []

    def enQueue(self, x):
        self.stack.insert(0, x)
    
    def deQueue(self):
        if not self.stack:
            return 
        x = self.stack[0]
        self.stack.pop(0)
        if not self.stack:
            return x
        item = self.deQueue()
        self.stack.insert(0, x)
        return item

def pathSum(self, root, sum):
    if not root:
        return []
    stack = [(root, root.val, [root.val])]
    ans = []
    while stack:
        node, val, val_list = stack.pop()
        if not node.left and not node.right and val == sum:
            ans.append(val_list)
        if node.right:
            val_list1 = val_list.copy()
            val_list1.append(node.right.val)
            stack.append((node.right, val+node.right.val, val_list1))
        if node.left:
            val_list.append(node.left.val)
            stack.append((node.left, val+node.left.val, val_list))
    return len(ans)

def maxSubArray(a, n):
    max_so_far = -100000
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(n):
        max_ending_here += a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    return max_ending_here, start, end

def str2num(s):
    l = len(s)
    ans = 0; i = 0
    while i < l:
        if s[i] == "1":
            ans += 1
        ans *= 2
        i += 1
    return ans//2

def num2str(n):
    x = n
    ans = ''
    while x>0:
        if x%2 == 1:
            ans += "1"
        else:
            ans += "0"
        x = x//2
#    ans += str(x%2)
    return ans
        
def swapLLpairs(head):
    temp = head
    if temp is None:
        return None
    while temp is not None and temp.next is not None:
        temp.data, temp.next.data = temp.next.data, temp.data
        temp = temp.next.next
    return head

# function to detect cycel in linked list and the the head of the cycle
def cycleLinkedList(head):
    slow = head
    fast = head
    while fast.next is not None and slow and fast:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            print("Found Loop")
            return True, slow
    return False, None
    
    
llist = Node(12)
llist = push(llist, 20) 
llist = push(llist, 4) 
llist = push(llist, 15) 
llist = push(llist, 10) 
   
# Create a loop for testing 
llist.next.next.next.next = llist

x, boo = cycleLinkedList(llist)

print(x, boo.data)

import sys

def buySellStocks(prices):
    minPrice = 100000
    maxProfit = -1
    for i in range(len(prices)):
        if prices[i] < minPrice:
             minPrice = prices[i]
        else if prices[i] - minPrice > maxProfit:
            maxProfit = prices[i] - minPrice
    return maxProfit