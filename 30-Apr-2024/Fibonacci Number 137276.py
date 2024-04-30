# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        i = self.fib(n - 1)
        j = self.fib(n - 2)
        return i + j