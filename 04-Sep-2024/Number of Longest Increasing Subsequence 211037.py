# Problem: Number of Longest Increasing Subsequence - https://leetcode.com/problems/number-of-longest-increasing-subsequence/

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        ct = defaultdict(list)
        ct[0] = [1,1]
        length, longest, answer = len(nums), 1, 1

        for right in range(1, length):
            map, cur_longest = defaultdict(lambda:1), 1
            for left in range(right-1, -1, -1):
                if nums[right] > nums[left] and ct[left][0] + 1 >= cur_longest:
                    temp_long, temp_ct = ct[left]
                    cur_longest = temp_long + 1
                    map[cur_longest] += temp_ct

            if map:
                map[cur_longest] -= 1
                ct[right] = [cur_longest, map[cur_longest]]

            else:
                ct[right] = ct[0]

            if cur_longest > longest:
                longest, answer = cur_longest, map[cur_longest]
            
            elif cur_longest == longest:
                answer += map[cur_longest]

        return answer
        