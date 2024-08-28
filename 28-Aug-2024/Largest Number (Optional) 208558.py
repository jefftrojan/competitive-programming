# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, num in enumerate(nums):
            nums[i] = str(num)
        
        def compare(n1, n2):
            if n1+n2 > n2+n1:
                return -1
            else:
                return 1
        
        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int(str(''.join(nums))))