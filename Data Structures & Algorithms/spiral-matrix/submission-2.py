class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []

        if len(matrix) == 1:
            return matrix[0]

        if len(matrix[0]) == 1:
            return [matrix[0][i] for i in range(len(matrix[0]))]
        
        elems = [matrix[0][0]]

        for i in range(1, len(matrix[0]) - 1):
            elems += [matrix[0][i]]

        elems += [matrix[0][-1]]

        for i in range(1, len(matrix) - 1):
            elems += [matrix[i][-1]]

        elems += [matrix[-1][-1]]

        for i in range(len(matrix[-1]) - 2, 0, -1):
            elems += [matrix[-1][i]]

        elems += [matrix[-1][0]]

        for i in range(len(matrix) - 2, 0, -1):
            elems += [matrix[i][0]]

        return elems + self.spiralOrder([mat[1:-1] for mat in matrix[1:-1]])