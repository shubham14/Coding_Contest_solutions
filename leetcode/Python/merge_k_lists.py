class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def mergeLists(self, head1, head2):
			a = head1
			b = head2
			res = None
			if a == None:
				return b
			if b == None:
				return a
			if a.val <= b.val:
				res = a
				res.next = self.mergeLists(a.next, b)
			else:
				res = b
				res.next = self.mergeLists(a, b.next)
			return res

	def mergeKLists(self, lists):
		last = len(lists)
		while last != 0:
			i = 0
			j = last
			while i < j:
				lists[i] = self.mergeLists(lists[i], lists[j])
				i += 1
				j -= 1
				if i >= j:
					last = j

		return lists[0]