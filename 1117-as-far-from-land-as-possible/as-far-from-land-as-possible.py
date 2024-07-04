class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = []
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    queue.append((i,j))
        cnt = 0
        while queue:
            temp_queue = queue
            queue = []
            for i,j in temp_queue:            
                if i - 1 >= 0 and grid[i-1][j] == 0:
                    grid[i-1][j] = 1
                    queue.append((i-1, j))
                if j - 1 >= 0 and grid[i][j - 1] == 0:
                    grid[i][j - 1] = 1
                    queue.append((i, j - 1))
                if i + 1 < n and grid[i + 1][j] == 0:
                    grid[i + 1][j] = 1
                    queue.append((i + 1, j))
                if j + 1 < n and grid[i][j + 1] == 0:
                    grid[i][j + 1] = 1
                    queue.append((i, j + 1))
            cnt+=1
        return cnt - 1 if cnt != 1 else -1 

