# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        lrg=max(nums)
        sml=min(nums)
        val=1
        if sml==lrg:
            return sml
        else:
            for i in range(2,sml+1):
                if sml%i==0 and lrg%i==0:
                    val=i 

        return val
        