# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        n = len(grid)
        m = len(grid[0])

        pathsmatrix = [[0]*m for i in range(n)]

        if grid[0][0] == 1:
            pathsmatrix[0][0] = 0
        else:
            pathsmatrix[0][0] = 1

        for i in range(1,m):
            if grid[0][i] == 1:
                pathsmatrix[0][i] = 0
            else:
                pathsmatrix[0][i] = pathsmatrix[0][i-1]
        for i in range(1,n):
            if grid[i][0] == 1:
                pathsmatrix[i][0] = 0
            else:
                pathsmatrix[i][0] = pathsmatrix[i-1][0]
        for i in range(1,n):
            for j in range(1,m):
                if grid[i][j] == 1:
                    pathsmatrix[i][j] = 0
                else:
                    pathsmatrix[i][j] = pathsmatrix[i][j-1] + pathsmatrix[i-1][j]
        return pathsmatrix[n-1][m-1]

            
        
        