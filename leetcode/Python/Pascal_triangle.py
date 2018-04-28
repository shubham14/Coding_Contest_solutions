import math

class Solution:

	def combination(self, n, r): # correct calculation of combinations, n choose k
	    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

	def for_test(self, x, y): 
	    for y in range(x):
	        return combination(x, y)

	def pascals_triangle(self, rows):
	    result = [] # need something to collect our results in
	   
	    for count in range(rows): 
	    	row = [] # need a row element to collect the row in
	        for element in range(count + 1): 
	            row.append(combination(count, element))
	        result.append(row)
	    return result

	for row in pascals_triangle(3):
	    print(row)

if __name__ == "__main__":

	Solution sol
	rows = 5
	sol.pascals_triangle(rows)