from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS from ecah non-rotten fruit

        minutes = 0 # minutes = -1
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                # BFS from (r, c) if it's a rotten fruit; if can't reach fresh then return -1
                if grid[r][c] != 1:
                    continue

                queue = deque()
                queue.append((0, (r, c)))
                visited = set()
                reached_fresh = False

                while len(queue) > 0:
                    dist, (row, col) = queue.popleft()

                    if grid[row][col] == 0:
                        continue

                    if grid[row][col] == 2:
                        minutes = max(minutes, dist)
                        reached_fresh = True
                        break

                    visited.add((row, col))

                    if row > 0:
                        if (row-1, col) not in visited:
                            queue.append((dist+1, (row-1, col)))

                    if row + 1 < len(grid):
                        if (row+1, col) not in visited:
                            queue.append((dist+1, (row+1, col)))

                    if col > 0:
                        if (row, col-1) not in visited:
                            queue.append((dist+1, (row, col-1)))

                    if col + 1 < len(grid[0]):
                        if (row, col + 1) not in visited:
                            queue.append((dist+1, (row, col+1)))

                if not reached_fresh:
                    return -1

        return minutes