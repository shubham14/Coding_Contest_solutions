class Solution:
	def binaryTreeRightView(self, root):
		if root is None:
			return
		queue = []; ans = []
		queue.append(root)
		while len(queue) != 0:
			n = len(queue)
			for i in range(n):
				temp = queue[0]
				queue.pop(0)
				if i == n-1:
					ans.append(temp.val)
				if temp.left is not None:
					queue.append(temp.left)
				if temp.right is not None:
					queue.append(temp.right)
		return ans


