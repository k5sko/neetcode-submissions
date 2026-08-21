class Solution:
    def reverseBits(self, n: int) -> int:
        sol = 0
        for i in range(32):
            sol <<= 1
            sol += ((n >> i) & 1)

        return sol