class Solution:
	def maxProfit(self, prices):
		MinEle = 10000
		MaxEle = 0
		for i in range(len(prices)):
			if prices[i] < MinEle:
				MinEle = prices[i] 
			elif prices[i] - MinEle > MaxEle:
				MaxEle = prices[i] - MinEle
		return MaxEle

if __name__ == "__main__":

	sol = Solution()
	prices = [7,1,5,3,6,4]
	ans = sol.maxProfit(prices)
	print(ans)
