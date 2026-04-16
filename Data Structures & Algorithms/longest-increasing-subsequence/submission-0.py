class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # lets try dp
        # bottom up seems easy to reason about here
        dp = [1 for _ in range(len(nums)+1)] # length of longest strictly increasing subsequence up to and including this element (and we count this element); dp[0] = 0 elements
        for idx in range(1, len(nums)+1):
            for j in range(idx):
                if nums[idx-1] > nums[j]:
                    dp[idx] = max(dp[idx], 1 + dp[j+1])

        return max(dp)