# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp = head
        prev = None
        while(temp.next and temp.val != val):
            temp = prev
            temp = temp.next

        prev.next = temp.next
        delete(temp)