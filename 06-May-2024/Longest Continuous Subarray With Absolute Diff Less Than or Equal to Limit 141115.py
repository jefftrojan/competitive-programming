# Problem: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/

from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxQueue = deque()
        minQueue = deque()
        
        length = len(nums)
        
        i = 0
        maxSize = 0
        
        for j, num in enumerate(nums):
            while maxQueue and maxQueue[-1] < num:
                maxQueue.pop()
            
            maxQueue.append(num)
            
            while minQueue and minQueue[-1] > num:
                minQueue.pop()
                
            minQueue.append(num)
            
            while maxQueue[0] - minQueue[0] > limit:
                if maxQueue[0] == nums[i]:
                    maxQueue.popleft()
                if minQueue[0] == nums[i]:
                    minQueue.popleft()
                
                i += 1
            maxSize = max(maxSize, j - i + 1)
        return maxSize