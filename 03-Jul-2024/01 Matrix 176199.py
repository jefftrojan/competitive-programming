# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        q = deque((i,j) for j in range(n) for i in range(m) if mat[i][j] == 0)
        map = [[0 if mat[i][j] == 0 else None for j in range(n)] for i in range(m)]
        while q:
            i,j = q.popleft()
            for n_i,n_j in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= n_i < m and 0 <= n_j < n and map[n_i][n_j] == None:
                    map[n_i][n_j] = map[i][j] + 1
                    q.append((n_i,n_j))
        return map