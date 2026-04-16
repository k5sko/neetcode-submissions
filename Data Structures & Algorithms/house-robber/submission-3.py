class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Think about bottom up.
        """
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        num_houses = len(nums)
        prev3 = 0
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])

        for idx in range(2, num_houses):
            prev3, prev2, prev1 = prev2, prev1, max(prev1, prev2+nums[idx], prev3 + nums[idx])

        return prev1
