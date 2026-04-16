class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()

        for i in range(len(nums)):
            num = nums[i]
            map[target - num] = i

        for i in range(len(nums)):
            num = nums[i]
            if num in map and i != map[num]:
                return [i, map[num]]