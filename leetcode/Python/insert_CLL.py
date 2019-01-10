class Node:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def __init__(self):
		self.head = None

	def count(self):
		c = 0
		if self.head is None:
			return 0
		temp = self.head
		while temp.next != self.head:
			c += 1
			temp = temp.next
		return c

	def push(self, x, pos):
		try:
			# pos = pos % self.count()
			c = 0
			temp = self.head
			while c != pos: 
				temp = temp.next
				c += 1
			xNode = Node(x)
			xNode.next = temp.next
			temp.next = xNode
		except ZeroDivisionError:
			temp = Node(x)
			self.head = temp
			temp.next = self.head

	def printList(self):
		temp = self.head
		if self.head is not None: 
			while(True):
				print ("%d" %(temp.val)) 
				temp = temp.next
				if (temp == self.head):
					break

if __name__ == "__main__":
	cllist = Solution() 
  	
	# Created linked list will be 11->2->56->12 
	cllist.push(12, 1) 
	cllist.push(56, 2) 
	cllist.push(2, 2) 
	cllist.push(11, 1) 
	  
	print "Contents of circular Linked List"
	# cllist.printList() 
	print (cllist.head.val)
	print (cllist.head.next.val)
	print (cllist.head.next.next.val)
	print (cllist.head.next.next.next.val)
