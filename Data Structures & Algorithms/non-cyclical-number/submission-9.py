class Solution:
    def isHappy(self, n: int) -> bool:
        vals = set()
        vals.add(1)

        while n not in vals:
            vals.add(n)
            n = self.sumOfSquares(n)

        return n == 1

    def sumOfSquares(self, n: int) -> int:
        res = 0

        while n > 0:
            res += (n%10) ** 2
            n //= 10

        return res