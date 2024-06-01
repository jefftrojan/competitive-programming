# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        start = 0
        end = n * m -1
        while (start <=  end):
            mid = (start + end)//2
            i = mid // m
            j = mid % m
            if (target == matrix[i][j]):
                return True
            elif (target < matrix[i][j]):
                end = mid -1
            else:
                start = mid + 1
        return False