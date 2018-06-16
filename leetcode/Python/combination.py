class Solution(object):
    def combinationSum(self, candidates, target):
    	ans = []
    	candidates.sort()
    	def backTracking(candidates, target, res):
    		if sum(res) == target:
    			ans.append(res)
    			return 
    		if sum(res) > target:
    			return 

    		for index, val in enumerate(candidates):
    			if sum(res) + val > target:
    				break
    			backTracking(candidates[index:], target, res)
    	backTracking(candidates, target, [])
    	return ans