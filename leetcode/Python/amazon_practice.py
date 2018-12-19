import numpy as np
from collections import defaultdict

# Linked list node
class Node:
    def __init__(self, x):
        self.x = x
        self.next = None

class Solution:
    def duplicateStrings(self, str):
        d = defaultdict(int)
        ans = ''
        for ch in str:
            if d[ch] %2 == 1:
                ans += ch
            d[ch] += 1
        return ans

    # helpeer function to reverse the linked list
    def reverseLinkedlist(st):
        curr = st
        prev = None
        next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        st = prev
        return st
        
    # input argument as the head pointer
    def revSecondHalfLinkedList(self, head):
        slow = head
        fast = head
        while slow is not None or fast is not None:
            slow = slow.next
            fast = fast.next.next
        revLL = self.reverseLinkedlist(slow.next)
        slow.next = revLL
        return head

if __name__ == "__main__":
    sol = Solution()
    print (sol.duplicateStrings("you got beautiful eyes"))