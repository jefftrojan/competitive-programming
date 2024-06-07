# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        res = [[]]
        i = 0
        while i < len(nums):
            count = 1
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                count += 1
                i += 1
            pre_length = len(res)
            for j in range(pre_length):
                sub_res = res[j][:]
                for x in range(1, count + 1):
                    if x > 0:
                        sub_res.append(nums[i])
                    res.append(sub_res[:])
            i += 1
        return res