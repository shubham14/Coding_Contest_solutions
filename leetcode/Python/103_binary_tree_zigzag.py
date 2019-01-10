class TreeNode:
	def __init__(self, x):
		self.val = x
		self.right = None
		self.left = None

class Solution:
	def zigzagLevelOrder(self, root):
		l = []; queue = []
		if root is None:
			return []
		else:
			queue.append(root):
			while len(queue) != 0:
				count = 0
				for i in range(len(queue)):
					l_int = []
					t = queue[0]
					queue.pop(0)
					if count == 0:
						l_int.append(t.val)
					elif count%2 == 0:
						if t.left is not None:
							l_int.append(t.left)
						if t.right is not None:
							l_int.append(t.right)
					elif count%2 == 1:
						if t.right is not None:
							l_int.append(t.right)
						if t.left is not None:
							l_int.append(t.left)
					l.append(l_int)
				count += 1
		return l