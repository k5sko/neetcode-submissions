class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        
        res = set()
        for idx in range(len(nums)):
            val = nums[idx]
            l, r = idx+1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + val == 0:
                    res.add((nums[l], nums[r], val))
                    l+=1
                    r-=1
                elif nums[l] + nums[r] + val < 0:
                    l+=1
                else:
                    r-=1
        return list(res)
