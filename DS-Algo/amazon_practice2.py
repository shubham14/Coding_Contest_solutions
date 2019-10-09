# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 00:18:18 2019

@author: Shubham
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
   
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

     
def symTree(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None:
        if root1.val == root2.val:
            return symTree(root1.left, root2.right) and symTree(root1.right, root2.left)
    return False

def push(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    head = new_node
    return head

llist = Node(12)
llist = push(llist, 20) 
llist = push(llist, 4) 
llist = push(llist, 15) 
llist = push(llist, 10) 
   

def revSecondHalf(head):
    slow = fast = head
    c = 0
    while slow.next and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        c += 1
    head = reverseBetween(head, c+1, 2*c)
    return head


def reverseSecondHalf(head):
    if head is None:
        return None
    slow = fast = head
    c = 0
    while slow.next and fast and fast.next:
        new_prev = slow
        slow = slow.next
        fast = fast.next.next
        c += 1
    
    tail, con = curr, new_prev
    while c + 1:
        next = curr.next
        curr.next = new_prev
        new_prev = curr
        curr = next
        c -= 1
    
    head = new_prev
    tail.next = curr
    return head
    

def reverseBetween(head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """

    # Empty list
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