from functools import cache

class Solution:
    def myPow(self, x: float, n: int) -> float:
        @cache
        def powHelper(x, n):
            if n == 1:
                return x
            elif n == 0:
                return 1

            if n%2==0:
                return self.myPow(x, n//2) * self.myPow(x, n//2)
            else:
                return self.myPow(x, n//2) * self.myPow(x, n//2) * x

        if n > 0:
            return powHelper(x, n)
        else:
            return 1/powHelper(x, -n)