class Solution:
    def highestPeak(self, isWater):
        m, n = len(isWater), len(isWater[0])
        queue, seen = [], set()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((i, j))
                    seen.add((i, j))
                    isWater[i][j] = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.pop(0)
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= x < m and 0 <= y < n and (x, y) not in seen:
                        queue.append((x, y))
                        seen.add((x, y))
                        isWater[x][y] = isWater[i][j] + 1
        return isWater
        