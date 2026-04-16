class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        max_sum = float('-inf')

        for num in nums:
            curr += num

            max_sum = max(curr, max_sum)

            if curr < 0:
                curr = 0


        return max_sum