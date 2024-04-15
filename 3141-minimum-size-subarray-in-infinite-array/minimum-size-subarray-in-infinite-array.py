class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans_1, target = divmod(target, sum(nums))
        ans_1 *= n
        if not target:
            return ans_1
        sum_n, m = 0, 0
        while sum_n <= target:
            sum_n += nums[m]
            m += 1
        m += n
        left, sum_n, ans_2 = 0, 0, inf
        for i in range(m):
            sum_n += nums[i%n]
            while left < m and sum_n >= target:
                if sum_n == target:
                    ans_2 = min(i-left+1, ans_2)
                sum_n -= nums[left%n]
                left += 1
        return -1 if ans_2 == inf else ans_1 + ans_2    