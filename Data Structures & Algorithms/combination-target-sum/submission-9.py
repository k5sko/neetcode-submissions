class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # just DP over target
        dp = [list() for _ in range(target+1)] # [[[]], [], [], [], [], [], [], [], [], []]
        dp[0] = [list()]
        nums.sort() # [2, 5, 6, 9]
        """
        for idx in range(1, target+1):
            for num in nums:
                if num > target:
                    break

                for combos in dp[idx-num]:
                    dp[idx].append(combos + [num]) 
        """
        for num in nums:
            for t in range(num, target+1):
                for combo in dp[t-num]:
                    dp[t].append(combo+[num])
                
        return dp[-1]