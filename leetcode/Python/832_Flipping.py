import numpy as np

class Solution():

	def FlipMatrix(self, A):
		n = len(A)
		XOR_mat = np.ones((n,n))

		# A matrix of all ones XORing with which will allow the
		# elements to be reversed
		XOR_mat = XOR_mat.tolist()
		B = []
		for row in A:
			B.append(reversed(row))

		B = map(lambda x,y: x^y, A, XOR_mat)
		return B

if __name__ == "__main__":

	# Instantiating a class object
	sol = Solution()
	A = [[1,1,0],[1,0,1],[0,0,0]]
	B = FlipMatrix(A)
