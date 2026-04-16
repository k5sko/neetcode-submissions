class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Let's try a DFS based soln.

        # we should do backtracking so that we can edit the number of indices we've covered so far in the string

        visited = set()
        indicesCovered = 0

        def dfs(r: int, c: int) ->  bool:
            nonlocal indicesCovered, visited
            # indicesCovered variable represents the number of chars in the string we've been able to cover
            if indicesCovered == len(word):
                return True

            if (r, c) in visited:
                return False

            if r < 0 or r >= len(board):
                return False

            if c < 0 or c >= len(board[r]):
                return False
            
            if board[r][c] == word[indicesCovered]:
                visited.add((r, c))
                indicesCovered+=1
                if dfs(r+1, c) or dfs(r-1, c) or dfs(r, c+1) or dfs(r, c-1):
                    return True
                visited.discard((r, c))
                indicesCovered -= 1
            else:
                return False



        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0] and dfs(row, col):
                    return True
        return False
