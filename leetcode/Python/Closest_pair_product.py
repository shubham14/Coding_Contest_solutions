import numpy as np
import math

class Solution:

	# arr is the list
	def closestPairProduct(self, arr, prod):
		arr.sort()
		l = 0
		r = len(arr)
		max_diff = 100000
		while(l < r):
			mul = arr[l] * arr[r]
			if math.abs(mul - prod) < max_diff:
				diff = math.abs(mul - prod)
			if mul < prod:
				r -= 1
			else:
				l += 1
		return (arr[l], arr[r])   

if __name__ == "__main__":
	arr = [1,3,5,7,43,8]
	prod = int(raw_input())
	sol = Solution(arr, prod)
	(l, r) = sol.closestPairProduct()
	print l, r