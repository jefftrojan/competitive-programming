# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i, r in enumerate(grid):
            for j, c in enumerate(r):
                if i and j:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                elif i:
                    grid[i][j] += grid[i-1][j]
                elif j:
                    grid[i][j] += grid[i][j-1]
        return grid[-1][-1]