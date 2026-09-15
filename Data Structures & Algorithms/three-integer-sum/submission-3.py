class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from collections import defaultdict
        
        triplets = set()
        sums = dict()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sums[-nums[i] - nums[j]] = (i, j)

        for key in sums:
            for idx in range(len(nums)):
                i, j = sums[key]
                if nums[idx] == key and idx != i and idx != j:
                    triplets.add(tuple(sorted((nums[i], nums[j], nums[idx]))))
        return list(triplets)