class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        There is a clear backtracking method; we simply add at a given step and subtract at the same step, nad see how many ways each yields.
        """
        #dp = [[0 for i in range(2*totalSum + 1)] for j in range(len(nums))]
        #dp = [defaultdict(int) for i in range(len(nums)+1)] # we are creating a dictionary for every potential index of nums; we start out at index 0 and see how many we can add at each level.
        # instead of dp full table, lets just use two defaultdicts()
        prev = defaultdict(int) # corresponds to target = 0
        curr = defaultdict(int) # corresponds to target = 1

        prev[0] = 1

        #dp[0][0] = 1 # How many ways are there to reach target of 0 when we are using 0 elements? Exactly 1. However, for every target number other than 0, we cannot reach it using 0 elements.
        idx = 0
        
        # now lets do bottom up dp
        while idx < len(nums): # we want to iterate for every possible number of elements included, from no elements included to all elems included
            # now, we are going to define dp[idx]
            # what we need to note is that for every sum we were able to get with idx-1, using idx, we can get two variants: sum[idx-1] + idx, sum[idx-1] - idx
            curr = defaultdict(int)
            for elem in prev: # each elem is a key
                curr[elem+nums[idx]] += prev[elem]
                curr[elem-nums[idx]] += prev[elem]

            prev = curr
            idx+=1

        return curr[target]