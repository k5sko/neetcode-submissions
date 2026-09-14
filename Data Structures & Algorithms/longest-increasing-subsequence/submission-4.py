class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1] * n
        
        for i in range(n, -1, -1):
            for j in range(i, n):
                if nums[i] < nums[j]:
                    length[i] = max(1 + length[j], length[i])

        return max(length)