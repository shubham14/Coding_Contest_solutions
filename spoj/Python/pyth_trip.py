import numpy as np

# complexiety is O(n^2)
class Solution:
	def findTrip(self, l):
		# squaring the array
		flag = 0
		l = list(map(lambda x: x ** 2, l)) # for python 3 compatibility
		l.sort() #sorting the array
		start = 0
		end = len(l) - 1
		i = 1
		for i in range(len(l)-1, 1, -1):
			while(start < end):
				if l[start] + l[end] == l[i]:
					ans = (l[start], l[end], l[i])
					flag = 1
					break
				elif l[start] + l[end] < l[i]:
					start += 1
				elif l[start] + l[end] > l[i]:
					end -= 1
		i += 1
		ans = (-1, -1, -1)

		if flag == 1:
			return True, ans
		return False, ans		

# main function
if __name__ == "__main__":
	l = [1,3,2,4,5]
	sol = Solution()
	bool_val, ans = sol.findTrip(l)
	print bool_val, ans