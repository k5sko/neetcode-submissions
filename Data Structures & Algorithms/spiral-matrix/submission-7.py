class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1

        elems = []

        while l < r and t < b:
            elems += [matrix[t][l]]
            for i in range(l+1, r):
                elems += [matrix[t][i]]

            elems += [matrix[t][r]]

            for i in range(t+1, b):
                elems += [matrix[i][r]]

            elems += [matrix[b][r]]
            for i in range(r-1, l, -1):
                elems += [matrix[b][i]]

            elems += [matrix[b][l]]
            for i in range(b-1, t, -1):
                elems += [matrix[i][l]]

            l += 1
            t += 1
            r -= 1
            b -= 1

        if l == r:
            elems += [matrix[i][l] for i in range(t, b+1)]
        elif t == b:
            elems += matrix[t][l:r+1]

        return elems

        """
        l, r = 0, 2
        t, b = 0, 2

        elems = [1, 2, 3, 6, 9, 8, 7, 4]
        """