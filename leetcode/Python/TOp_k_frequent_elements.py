from collections import Counter

class Solution:
    def kFrequentElements(self, nums, k):
        ans = []
        c = dict(Counter(nums))
        for keys in list(c.keys()):
            if c[keys] >= k: 
                ans.append(keys)
        return ans

    def array_partition_1(self, nums):
        nums.sort()
        s = sum([nums[i] for i in range(1, len(nums), 2)])
        return s

    def kthSmallest(self, root, k):
        self.k = k
        self.result = None
        self.inorder(root)
        return self.result

    def inorder(self, node):
        if node.left:
            self.inorder(node.left)
        self.k -= 1
        if self.k == 0:
            self.result = node.val
            return 
        if self.result:
            return
        if node.right:
            self.inorder(node.right)
        


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    sol = Solution()
    ans = sol.kFrequentElements(nums, k)
    print (ans)