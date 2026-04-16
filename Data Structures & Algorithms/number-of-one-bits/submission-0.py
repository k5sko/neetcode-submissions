class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            new = n >> 1
            if new == (n-1)//2:
                count += 1
            n = new
        return count