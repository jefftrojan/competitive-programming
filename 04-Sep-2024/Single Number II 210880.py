# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self,nums:List[int])->int:
        return (sum(set(nums))*3 -sum(nums))//2        