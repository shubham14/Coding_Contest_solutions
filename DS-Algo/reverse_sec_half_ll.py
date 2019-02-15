import numpy as np

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, x):
        t = Node(x)
        if self.head is None:
            self.head = t
        else:
            t.next = self.head
            self.head = t

    # reverse Linked List Util function for a general list
    def reverseLL(self, head):
        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head
        
    def reverse_secondHalf(self):
        slow = fast = temp = self.head
        while slow and fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = self.reverseLL(slow)
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next
        # print(temp.val)
        

if __name__ == "__main__":
    # instantaiate the list with the following elements
    llist = LinkedList()
    llist.push(20) 
    llist.push(4) 
    llist.push(15) 
    llist.push(85)
    llist.push(30)
    llist.push(100)

    llist.printList()
    print("----------------")
    llist.reverse_secondHalf()
    llist.printList()