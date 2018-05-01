from operator import itemgetter
import numpy as np
import pandas as pd
import sys

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

	def hasCycle(self, head):

		# employing fast pointer algorithm
		ListNode node
		node fast, slow
		fast = head
		slow = head
		while(fast.next != None):
			slow = slow.next
			fast = fast.next.next
			if(slow.val == fast.val):
				return True
		return False
