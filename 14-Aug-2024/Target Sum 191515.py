# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def recur(i, summ):
            if i < 0:
                if summ == target:
                    return 1
                return 0
            negative = recur(i-1, summ-nums[i])
            positive = recur(i-1, summ+nums[i])
            return negative + positive
        return recur(len(nums)-1, 0)