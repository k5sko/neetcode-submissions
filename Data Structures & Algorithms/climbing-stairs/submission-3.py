class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [None] * (n+1)

        def countWays(n):
            if n == 0 or n == 1:
                return 1
            elif n < 0:
                return 0

            if memo[n-1]:
                one_step = memo[n-1]
            else:
                one_step = countWays(n-1)
                memo[n-1] = one_step

            if memo[n-2]:
                two_step = memo[n-2]
            else:
                two_step = countWays(n-2)
                memo[n-2] = two_step

            return one_step + two_step

        return countWays(n)