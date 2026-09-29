class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pos, neg = 0, 0 # 8, 8
        product = max(nums) # 5

        for num in nums: # -3
            if num == 0:
                product = max(product, neg, pos)
                pos, neg = 0, 0
            elif num < 0:
                if neg < 0:
                    product = max(product, neg * num)
                    tmp = pos
                    pos = neg * num
                    neg = tmp * num
                elif neg == 0: # only other case
                    neg = min(num, num * pos)
                    pos = 0
            else:
                if pos == 0:
                    pos = num 
                else:
                    pos *= num
        
                if neg < 0:
                    neg *= num
                
                product = max(product, pos)
                
        return product