# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid); col = len(grid[0])
        res = 0
        
        def dfs(i, j):
            if ( not 0 <= i < row) or (not 0 <= j < col) or (grid[i][j] == '0'): return
            grid[i][j] = '0'
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        
        return res
    