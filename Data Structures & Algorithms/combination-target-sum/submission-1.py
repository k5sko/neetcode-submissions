class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        dp = [[[] for _ in range(n + 1)] for _ in range(target + 1)]

        # Base case: one way to make 0, the empty combination
        for i in range(n + 1):
            dp[0][i] = [[]]

        for t in range(1, target + 1):
            for i in range(1, n + 1):
                num = nums[i - 1]

                # Group 1: don't use num
                dp[t][i] = list(dp[t][i - 1])

                # Group 2: use num at least once (stay in column i so it can repeat)
                if num <= t:
                    for combo in dp[t - num][i]:
                        dp[t][i].append(combo + [num])

        return dp[target][n]