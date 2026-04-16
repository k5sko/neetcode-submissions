from collections import deque
class Solution:
    def islandsAndTreasure(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def bfs(gates):
            q = gates
            visited = set()

            while len(q) > 0:
                r, c, dist = q.popleft()
                if r >= len(rooms) or r < 0 or c >= len(rooms[r]) or c < 0: # if oob
                    continue

                if rooms[r][c] == -1 or (r, c) in visited: # if we've visited this node already in this bfs or this is a gate/wall
                    continue

                rooms[r][c] = dist
                visited.add((r, c))

                q.append((r+1, c, dist+1))
                q.append((r, c+1, dist+1))
                q.append((r-1, c, dist+1))
                q.append((r, c-1, dist+1)) 

        gates = deque()
        for row in range(len(rooms)):
            for col in range(len(rooms[row])):
                if rooms[row][col] == 0:
                    gates.append((row, col, 0))

        bfs(gates)