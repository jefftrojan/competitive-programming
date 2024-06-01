# Problem: Peak Index in a Mountain Array - https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid == 0:
                return mid + 1
            if mid == len(arr) - 1:
                return mid - 1
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                return mid
            if arr[mid-1] < arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
         