'''
Python program to find if a string has all unique charecters
'''
import numpy as np

class Solution:
	def uniqChar(self, str1):
	    for i in range(1,200):
	        for j in range(len(str1)):
	            s = map(lambda x: x - i, map(lambda y: ord(y), str1))
	            d = list(filter(lambda x: x == 0, s))
	            if len(d) > 1:
	                return False
	    return True

if __name__ == "__main__":
	sol = Solution()
	print (sol.uniqChar("ABCDEFGHIJKLMNOPARSTUVWXYZ"))