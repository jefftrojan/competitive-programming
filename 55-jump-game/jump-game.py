class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        destination = len(nums) - 1
        for i in range(len(nums) - 2 , -1 , -1):
            
            if nums[i] + i >= destination:
                destination = i

        return destination == 0