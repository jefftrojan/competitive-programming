# Problem: Sum of Subarray minimums - https://leetcode.com/problems/sum-of-subarray-minimums/


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        result = 0
        mod = 10**9 + 7

        for i, num in enumerate(arr):
            while stack and num < arr[stack[-1]]:
                idx = stack.pop()
                result += arr[idx] * (i - idx) * (idx - (stack[-1] if stack else -1))
                result %= mod

            stack.append(i)

        while stack:
            idx = stack.pop()
            result += arr[idx] * (len(arr) - idx) * (idx - (stack[-1] if stack else -1))
            result %= mod

        return result