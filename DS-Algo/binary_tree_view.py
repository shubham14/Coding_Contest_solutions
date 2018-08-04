import numpy as np

# node structure defined here
class TreeNode:
	def __init__(self, item):
		self.data = item
		self.left = None
		self.right = None

class Solution(TreeNode):

	# generalised function for both left and right views of the tree
	def ViewUtil(self, root, level, max_level, direc):
		node_vec = []
		if root is None:
			print ("Empty Tree Structure!!")
			return 
		else:
			if level > max_level:
				node_vec.append(root.data)
				max_level = level
			
			# the direction decided which child to visit first accordingly
			if direc == 'left':
				ViewUtil(root.left, level + 1, max_level)
				ViewUtil(root.right, level + 1, max_level)
			elif direc == 'right':
				ViewUtil(root.right, level + 1, max_level)
				ViewUtil(root.left, level + 1, max_level)

		return node_vec

	# driver function for the view of a binary tree
	def View(self, root, direc):
		level = 1
		max_level = 0
		ans = ViewUtil(root, level, max_level, direc)
		return ans

if __name__ == "__main__":
	