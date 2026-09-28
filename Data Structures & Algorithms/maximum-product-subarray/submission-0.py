class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_pos, min_neg = 1, 1
        max_prod = max(nums)
        # max_pos = 24, min_neg = -24
        for num in nums:
            if num < 0:
                if min_neg != 1: 
                    max_prod = max(max_prod, min_neg * num)
                    min_neg = num
                    max_pos = min_neg * num
                else: # min_neg = 1
                    min_neg = num
                    max_prod = max(max_prod, max_pos)
                    max_pos = 1
            elif num > 0:
                max_pos *= num
                min_neg *= num
            else: # num == 0
                max_prod = max(max_prod, max_pos)
                max_pos = 1
                min_neg = -1
                
        return max(max_prod, max_pos)