class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr = 0
        for num in nums:
            val = curr ^ num
            if val != 0:
                return curr

            curr += 1
        
        return curr