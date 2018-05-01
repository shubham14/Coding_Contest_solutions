class Solution:
	def maxDepth(self, root):
		# first two are the base cases with the tree be NULL 
		# or the node is a leaf node
		if (root == None):
			return 0
		elif root.left == None and root.right == None:
			return 1
		
		# check whether the node has a lef or right child
		elif root.right == None:
			return 1 + maxDepth(root.left)
		elif root.left == None:
			return 1 + maxDepth(root.right)

		# recursively move over left and right subtree
		else:
			return max(maxDepth(root.right), maxDepth(root.left)) + 1

# main function
if __name__  == "__main__":
	sol = Solution()
	
