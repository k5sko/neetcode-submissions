class Solution:
    def jump(self, nums: List[int]) -> int:
        # precompute the position you can reach from each
        reachable = []
        for idx in range(len(nums)):
            reachable.append(min(len(nums)-1, idx+nums[idx]))

        jumps = 0
        curr_idx = 0
        while curr_idx < len(nums) - 1:
            curr_idx = max(range(reachable[curr_idx], curr_idx, -1), key = lambda x: reachable[x])
            jumps += 1
        return jumps

"""
[2, 2, 4, 4, 4]
curr_idx = 2
jumps = 1

"""