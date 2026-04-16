class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        num_houses = len(nums)
        prev = nums[0]
        curr = max(nums[0], nums[1])

        for idx in range(2, num_houses):
            prev, curr = curr, max(curr, prev + nums[idx])

        return curr