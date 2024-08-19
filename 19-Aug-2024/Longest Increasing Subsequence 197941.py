# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

from functools import cache
class Solution:
    def lengthOfLIS(self, nums) -> int:
        @cache
        def dp(i):
            ans = 1

            for j in range(i):
                if nums[i] > nums[j]:
                    ans = max(ans, dp(j) + 1)
            
            return ans

        return max(dp(i) for i in range(len(nums)))   
            
            
        