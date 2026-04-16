class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        nums = nums[::-1]
        closest_that_reaches = 0
        hits = False

        for idx in range(n):
            if closest_that_reaches < idx - nums[idx]:
                hits = False
            else:
                closest_that_reaches = idx
                hits = True

        return hits

"""
n = 3
nums = [0, 0, 2]
closest_that_reaches = 0

idx = 0
0 - 0 = 0; closest_that_reaches = 0

idx = 1
0 < 1 - 0; 0 < 1 (YES)
"""