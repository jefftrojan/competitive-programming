class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)

        result = []
        for num in nums1:
            if num in next_greater:
                result.append(next_greater[num])
            else:
                result.append(-1)
        
        return result