class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # run dfs for each 1 to find the islands and then keep a set of visited indices to make sure you don't double count
        from collections import deque

        visited = set()

        num_islands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited and grid[i][j] == "1":
                    #dfs()
                    stack = deque()
                    stack.append((i, j))
                    while len(stack) > 0:
                        r, c = stack.pop()

                        if grid[r][c] == "0":
                            continue

                        visited.add((r, c))

                        if r + 1 < len(grid) and (r+1, c) not in visited:
                            stack.append((r+1, c))
                        if r - 1 >= 0 and (r-1, c) not in visited:
                            stack.append((r-1, c))

                        if c + 1 < len(grid[0]) and (r, c+1) not in visited:
                            stack.append((r, c+1))
                        if c - 1 >= 0 and (r, c-1) not in visited:
                            stack.append((r, c-1))

                    num_islands += 1

        return num_islands