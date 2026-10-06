class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # maybe at any point we can choose to either increase current index or we can 
        nums.sort()
        n = len(nums)
        dp = [[list() for _ in range(n+1)] for _ in range(target + 1)] 

        for i in range(n+1):
            dp[0][i].append([])

        for t in range(nums[0], target+1):
            for i in range(1, n+1):
                dp[t][i] = dp[t][i-1].copy()
                num = nums[i-1]      
                if num <= t:
                    for way in dp[t-num][i]:
                        dp[t][i].append(way+[num]) 
        
        return dp[-1][-1]