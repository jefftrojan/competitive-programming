# Problem: House Robber II - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(a,n):
            n=len(a)
            prev=a[0]
            prev2=0
            curr=0
            for i in range(1,n):
                pick=a[i]
                if i>1:
                    pick+=prev2
                non_pick=prev
                curr=max(pick,non_pick)
                prev2=prev
                prev=curr
            return prev
        if len(nums)==1:
            return nums[0]
        n=len(nums)
        return max(solve(nums[1:],n),solve(nums[:-1],n))