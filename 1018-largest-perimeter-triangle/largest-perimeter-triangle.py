class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)       
        i = n-1
        j = n-3
        while(j>=0):
            if(nums[j]+nums[j+1]>nums[i]):
                return nums[j]+nums[j+1]+nums[i]
            i=i-1
            j=j-1
        return 0