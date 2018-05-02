# Definition of the tree node
class TreeNode(object):

	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

#to optimize this solution further
class Solution:
	def sumNumbers(self, root):
		if root == None:
			return 0
		ans = 0
		l = []


