class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # my understanding: find the regions that don't connect to the edge of the board
        # maybe use dfs or a union-find
        # if dfs shows that any of the connected O's are on the edge of the board, then ignore it
        # add all regions to a set of visited
        from collections import deque

        visited = set()

        for r in range(len(board)):
            for c in range(len(board[r])):
                    if board[r][c] == "X":
                        continue
                    
                    if (r, c) in visited:
                        continue

                    stack = deque()
                    stack.append((r, c))

                    current_region = []
                    replace_0 = True

                    while len(stack) > 0:
                        r1, c1 = stack.pop()
                        visited.add((r1, c1))
                        current_region += [(r1, c1)]

                        if r1 == 0 or r1 == len(board) - 1 or c1 == 0 or c1 == len(board[r1]) - 1:
                            replace_0 = False

                        for y in [r1-1, r1+1]:
                            if y >= 0 and y < len(board):
                                if board[y][c1] == "O" and (y, c1) not in visited:
                                        stack.append((y, c1))
                        
                        for x in [c1-1, c1+1]:
                            if x >= 0 and x < len(board[0]):
                                if board[r1][x] == "O" and (r1, x) not in visited:
                                    stack.append((r1, x))

                    if replace_0:
                        for y, x in current_region:
                            board[y][x] = "X"
