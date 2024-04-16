# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         maxSum = nums[0]
#         currentSum = nums[0]

#         for num in nums[1:]:
#             currentSum = max(num, currentSum + num)
#             maxSum = max(maxSum, currentSum)

#         return maxSum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = 0
        overall_max = -inf
        for num in nums:
            current_max = max(current_max + num, num)
            overall_max = max(overall_max, current_max)
        return overall_max