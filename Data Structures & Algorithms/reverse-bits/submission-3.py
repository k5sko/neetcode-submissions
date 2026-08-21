class Solution:
    def reverseBits(self, n: int) -> int:
        return n ^ (2**32 - 1)