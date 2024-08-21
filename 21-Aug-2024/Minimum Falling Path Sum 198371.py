# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        duplicate = [[inf for _ in range(len(matrix))] for _ in range(len(matrix))]
        duplicate[0] = matrix[0].copy()
        for i in range(1, len(matrix)):
            duplicate[i][0] = min(duplicate[i-1][0], duplicate[i-1][1]) + matrix[i][0]
            duplicate[i][-1] = min(duplicate[i-1][-1], duplicate[i-1][-2]) + matrix[i][-1]
            for j in range(1, len(matrix)-1):
                duplicate[i][j] = min(duplicate[i-1][j-1], duplicate[i-1][j], duplicate[i-1][j+1]) + matrix[i][j]
        
        return min(duplicate[-1])
