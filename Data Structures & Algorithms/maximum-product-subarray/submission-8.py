class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pos, neg = 1, 1 # 8, 8
        max_prod = max(nums)
        for num in nums: # pos, neg = 0, -24
            pos, neg = max(num, num*pos, num*neg), min(num, num*pos, num*neg)
            max_prod = max(max_prod, pos)
        return max_prod