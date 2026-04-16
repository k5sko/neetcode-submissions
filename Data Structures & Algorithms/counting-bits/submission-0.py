class Solution:
    def countBits(self, n: int) -> List[int]:
        bin_num = 0
        res = [-1 for _ in range(n+1)]
        res[0] = 0
        for idx in range(1, n+1):
            if idx>>1 == (idx-1)//2:
                res[idx] = res[(idx-1)//2] + 1
            else:
                res[idx] = res[idx//2]

        return res