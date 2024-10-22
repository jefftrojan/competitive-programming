# Problem: Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        seen = []
        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            nums[i] = bisect.bisect_left(seen, n)
            seen.insert(nums[i], n)
        return nums