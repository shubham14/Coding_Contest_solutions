# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 20:51:55 2018

@author: Shubham
"""

# node structure
class Node:
    def __init__(self,x):
        self.val = x
        self.next = None
        
# linkedlist class
class LL:
    def __init__(self, head):
        self.head = head
        
    def printList(self):
        if self.head is None:
            print (-1)
        while self.head:
            print (self.head.val)
            self.head = self.head.next
    
    # insert function in the linked list
    def insert(self, x):
        temp = Node(x)
        if self.head is None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp
    


# class containing the logic for getting the intersection node
class Solution():
    # count the number of nodes in the linked list
    # helps offset the extra nodes
    def count(self, head):
        count = 0 
        while head:
            count += 1
        return count
    # return the value of the intersection node
    def get_intersect(self, head1, head2):
        c1 = self.count(head1)
        c2 = self.count(head2)
        if c1 > c2:
            temp1 = head1
            temp2 = head2
        else:
            temp1 = head2
            temp2 = head1
            
        for i in range(d):
            temp1 = temp1.next
        
        while temp1 and temp2:
            if temp1.val == temp2.val:
                return temp1.val
            else:
                temp1 = temp1.next
                temp2 = temp2.next
            return -1
    

if __name__ == "__main__":
    
    # list definitions
    head1 = Node(1)
    ll = LL(head1)
    ll.insert(3)
    ll.insert(5)
    ll.insert(7)
    print ("First Linked List")
    ll.printList()
    
    head2 = Node(1)
    ll1 = LL(head2)
    ll1.insert(3)
    ll1.insert(5)
    ll1.insert(6)
    print ("Second Linked List")
    ll1.printList()
    
    # intersection node
    sol = Solution()
    ans = sol.get_intersect(head1, head2)
    print(ans)