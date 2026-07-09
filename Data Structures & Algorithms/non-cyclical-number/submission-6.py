class Solution:
    def isHappy(self, n: int) -> bool:
        vals = set()
        vals.add(1)

        while n not in vals:
            vals.add(n)
            n = sumOfSquares(n)

        return n

    def sumOfSquares(self, n: int) -> int:
        res = 0

        while n > 0:
            res += (n%10) ** 2
            n //= 10

        return res