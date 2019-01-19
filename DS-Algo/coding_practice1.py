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
    c = 0
    fast = slow = head
    while fast.next.next is not None and slow.next is not None:
        fast = fast.next.next
        c += 1
        slow = slow.next
    print (c)
    head1 = reverseBetween(head, c, 2*c)
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
h = reverseBetween(head, 1, 4)
printList(h)

