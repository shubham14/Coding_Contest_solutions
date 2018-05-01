class Solution:

	def minimumTotal(self, Triangle):
		for row in range((len(triangle)-2), -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] = min(triangle[row][col]+triangle[row+1][col], triangle[row][col]+triangle[row+1][col+1])
		return triangle[0][0]