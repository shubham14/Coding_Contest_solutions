class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def getCount(head):
    c = 0
    temp = head
    while temp:
        c += 1
        temp = temp.next
    return c

def push(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    head = new_node
    return head

def getIntersection(head1, head2):
    d1 = getCount(head1)
    d2 = getCount(head2)
    temp1 = head1; temp2 = head2
    if d1 > d2:
        i = 0
        while i < d1 - d2:
            temp1 = temp1.next
            i += 1
    elif d2 > d1:
        i = 0
        while i < d2 - d1:
            temp2 = temp2.next
            i += 1
    while temp1.next is not None and temp2.next is not None:
        if temp1.val == temp2.val:
            return temp1.val
        temp1 = temp1.next
        temp2 = temp2.next
    return -1

def printList(head):
    temp = head
    while temp:
        print(temp.val)
        temp = temp.next

if __name__ == "__main__":
    head = Node(1)
    head = push(head, 2)
    head = push(head, 5)
    head = push(head, 3)
    head = push(head, 7)
    head = push(head, 9)

    head1 = Node(7)
    head1 = push(head1, 6)
    head1 = push(head1, 5)
    head1 = push(head1, 7)
 
    print ('--- Original List ---')
    printList(head)
    
    print ('--- Original List 1 ---')
    printList(head1)

    # print(getIntersection(head, head1))
    print("----Length of the list----")
    print (getCount(head1))