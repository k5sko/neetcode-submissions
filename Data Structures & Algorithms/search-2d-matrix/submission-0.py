class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        We can first do a binary search for the possible interval (row) it might lie in. Then, we can binary search within that row.
        """
        l, r = 0, len(matrix[0]) -1
        row = -1
        top, bottom = 0, len(matrix)-1

        while top <= bottom:
            m = top + (bottom - top)//2
            if target >= matrix[m][l] and target <= matrix[m][r]:
                row = m
                break
            elif target < matrix[m][l]:
                bottom = m-1
            else:
                top = m+1
        
        if row == -1:
            return False

        while l <= r:
            m = r + (l-r)//2
            if target == matrix[row][m]:
                return True
            elif target < matrix[row][m]:
                r = m-1
            else:
                l = m+1
        
        return False