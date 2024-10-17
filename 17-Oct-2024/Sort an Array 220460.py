# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        heapsize = len(nums)
        def heapify(idx: int): 
            while True:
                left = idx * 2 + 1
                right = idx * 2 + 2
                maxi = nums[idx]
                maxiIdx = idx
                if left < heapsize and nums[left] > maxi:
                    maxi = nums[left]
                    maxiIdx = left
                if right < heapsize and nums[right] > maxi:
                    maxi = nums[right]
                    maxiIdx = right

                if maxiIdx == right: 
                    nums[idx], nums[right] = nums[right], nums[idx]
                    idx = right
                elif maxiIdx == left:
                    nums[idx], nums[left] = nums[left], nums[idx]
                    idx = left
                else: break
            
        for i in range(n-1, -1, -1): 
            heapify(i)

        for i in range(n-1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapsize = i
            heapify(0)
        
        return nums