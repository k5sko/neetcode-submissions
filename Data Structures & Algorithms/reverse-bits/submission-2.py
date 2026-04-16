class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        idx = 32
        while n > 0:
            if n%2 == 1:
                res += 2**(idx-1)
            n = n>>1
            idx-=1

        return res