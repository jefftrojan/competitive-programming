# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            if nums.count(i)==1:
                a.append(i)
        return a
        