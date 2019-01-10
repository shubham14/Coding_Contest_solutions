class TreeNode:
	def __init__(self, x):
		self.val = x
		self.right = None
		self.left = None

class Codec:
	def serialize(self, root):
		l = []; queue = []
		if root is None:
			l.append('null')
		else:
			queue.append(root)
			while len(queue) != 0:
				t = queue[0]
				queue.pop(0)
				l.append(str(t.val))
				queue.append(t.left)
				queue.append(t.right)
		return l