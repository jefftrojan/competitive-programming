# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution(object):
        """
        :type nums: List[int]
        :rtype: int
        """
        def missingNumber(seelf, nums):
            n = len(nums)
            xor_all = 0
            xor_nums = 0
            
            # XOR all numbers from 0 to n
            for i in range(n + 1):
                xor_all ^= i
            
            # XOR all elements in the array
            for num in nums:
                xor_nums ^= num
            
            # The missing number is the XOR of xor_all and xor_nums
            return xor_all ^ xor_nums
