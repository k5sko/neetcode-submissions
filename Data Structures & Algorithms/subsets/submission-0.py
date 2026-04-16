class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        excludeFirst = self.subsets(nums[1:]) # []

        includeFirst = [
            [nums[0]] + i for i in excludeFirst
        ] # [[nums[0]]
        print(includeFirst)
        return includeFirst + excludeFirst

"""
[[], [2], [1], [1, 2]]
"""

"""
Goal: for each element, add a sublist where we include it and a sublist where we exclude it

[[], [1], [2], [1, 2]] + [[3], [1, 3], [2, 3], [1, 2, 3]]

[[2] + [3]] + [[3]]

[[1] + [[2, 3], [2]]]

[nums[0] + [i] in returned]
"""