# Problem: Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        minn=nums[0]
        if nums[0]<=nums[right]:
            return nums[0]
        while True:
            if left>=right:
                return minn
            mid=(left+right)//2
            if(nums[mid]<minn):
                minn=nums[mid]
            if nums[mid+1]<nums[mid]:
                return nums[mid+1]
            if (nums[mid-1]>nums[mid]):
                return nums[mid]
            if nums[mid]>nums[right]:
                left=mid+1
            if nums[mid]<nums[right]:
                right=mid-1
     

     
            