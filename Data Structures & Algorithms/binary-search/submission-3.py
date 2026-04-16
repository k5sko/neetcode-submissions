class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            mean = (l+r)//2
            if nums[mean] == target:
                return (l+r)//2
            elif nums[mean] < target:
                l = mean + 1
            else:
                r = mean 

        if l == r:
            if nums[l] == target:
                return l
            else:
                return -1
        return -1