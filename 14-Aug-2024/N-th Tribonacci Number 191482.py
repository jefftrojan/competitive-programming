# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        t0, t1, t2 = 0, 1, 1

        for i in range(n-2):
            t2, t1, t0 = t2+t1+t0, t2, t1
        
        return t2