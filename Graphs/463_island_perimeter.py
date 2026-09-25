class Solution(object):
    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 1

            if grid[r][c] == 0:
                return 1

            if grid[r][c] == -1:
                return 0

            grid[r][c] = -1

            return (
                dfs(r + 1, c) +
                dfs(r - 1, c) +
                dfs(r, c + 1) +
                dfs(r, c - 1)
            )

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)

        return 0