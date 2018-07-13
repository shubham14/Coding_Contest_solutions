
class Solution:

	# n is the degree of the polynomial
	def __init__(self, l, n):
		self.l = l
		self.n = n

	def find_intercept(self):
		n = self.n
		ans_check = True
		for i in range(1, len(l)):
			if l[i] == -(n-i):
				ans_check = ans_check and True
		if ans_check == True:
			return 0
		else:
			return false

