class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def secondHalf(self, head):
        fast = slow = head
        c = 1
        while fast.next.next is not None and slow.next is not None:
            fast = fast.next.next
            slow = slow.next
            c += 1
        return c

    def push(self, head, new_data):
        new_node = Node(new_data)
        new_node.next = head
        head = new_node
        return head

    def printList(self, head):
        temp = head
        while(temp):
            print (temp.data)
            temp = temp.next

    def reverseBetween(self, head, m, n):
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
    
    def reverseSecondHalf(self, head):
        c = self.secondHalf(head)
        head1 = self.reverseBetween(head, c+1, 2*c)
        return head1

if __name__ == "__main__":    
    sol = Solution()
    head = Node(1)
    head = sol.push(head, 2)
    head = sol.push(head, 5)
    head = sol.push(head, 3)
    head = sol.push(head, 7)
    head = sol.push(head, 9)

    print ('--- Original List ---')
    sol.printList(head)
    #
    print ('--- Reversed List ---')
    h = sol.reverseSecondHalf(head)
    sol.printList(h)

