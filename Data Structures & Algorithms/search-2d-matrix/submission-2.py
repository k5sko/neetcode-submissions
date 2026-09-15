class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search for the row by looking within bounds
        l, r = 0, len(matrix) - 1
        while l < r:
            m = (l + r)//2
            if matrix[m][0] <= target and target <= matrix[m][-1]:
                r = m
                break
            elif matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1

        # now we know r is the correct row

        i, j = 0, len(matrix[r]) - 1
        while i < j:
            m = (i + j)//2
            if matrix[r][m] == target:
                j = m
                break
            elif matrix[r][m] > target:
                j = m - 1
            else:
                i = m + 1

        return matrix[r][j] == target