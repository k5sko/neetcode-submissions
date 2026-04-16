class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0

        def dfs(row, col):
            # out of bounds
            if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0:
                return

            # at water not land
            if grid[row][col] == "0":
                return
                
            grid[row][col] = "0"

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)


        # n * m * 
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    counter+=1

        return counter
        