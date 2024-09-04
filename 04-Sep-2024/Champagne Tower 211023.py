# Problem: Champagne Tower - https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        pyramid = {k-1:[0] * k for k in range(1, 101)}
        pyramid[0][0] = poured
        for row in range(1, query_row+1):
            T = True
            for c in range(row):
                val = (pyramid[row-1][c] - 1.0) / 2.0
                if val>0:
                    T = False
                    pyramid[row][c] += val
                    pyramid[row][c+1] += val
            if T:
                return min(1, pyramid[query_row][query_glass])
        return min(1, pyramid[query_row][query_glass])