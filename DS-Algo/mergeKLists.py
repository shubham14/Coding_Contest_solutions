# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 11:50:49 2019

@author: Shubham
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def push(head, val):
    temp = Node(val)
    temp.next = head
    head = temp
    return head

def merge(L1, L2):
  
  # create new linked list pointer
  L3 = Node(None)
  prev = L3

  # while both linked lists are not empty
  while L1 != None and L2 != None:
    if L1.val <= L2.val:
      prev.next = L1
      L1 = L1.next
    else:
      prev.next = L2
      L2 = L2.next	
    prev = prev.next

  # once we reach end of a linked list, append the other 
  # list because we know it is already sorted
  if L1 == None:
  	prev.next = L2
  elif L2 == None:
  	prev.next = L1

  return L3.next

def printList(head):
    temp = head
    while temp:
        print(temp.val)
        temp = temp.next
#    print(temp.val)
    
if __name__ == "__main__":
    head1 = Node(7)
    head1 = push(head1, 6)
    head1 = push(head1, 5)
    head1 = push(head1, 5)
    head1 = push(head1, 4)
    head1 = push(head1, 3)
    head1 = push(head1, 2)
        
    head2 = Node(34)
    head2 = push(head2, 24)
    head2 = push(head2, 21)
    head2 = push(head2, 12)
    head2 = push(head2, 11)
    head2 = push(head2, 10)
    head2 = push(head2, 1)
    
    head3 = merge(head1, head2)
    printList(head3)