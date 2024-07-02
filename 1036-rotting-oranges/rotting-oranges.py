class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append([i, j])
        
        ans = -1
        while q:
            temp = q.copy()
            q.clear()
            for i, j in temp:
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    q.append([i - 1, j])
                    grid[i - 1][j] = 2
                if i + 1 < row and grid[i + 1][j] == 1:
                    q.append([i + 1, j])
                    grid[i + 1][j] = 2
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    q.append([i, j - 1])
                    grid[i][j - 1] = 2
                if j + 1 < col and grid[i][j + 1] == 1:
                    q.append([i, j + 1])
                    grid[i][j + 1] = 2
                grid[i][j] = 2
            ans += 1
        
        for i in grid:
            for j in i:
                if j == 1:
                    return -1
        return ans if ans >= 0 else 0