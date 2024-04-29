class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l = 0
        res = 0
        from collections import deque
        inc = deque()
        dec = deque()
        for r in range(len(nums)):
            while (dec and dec[0] - nums[r] > 2) or (inc and nums[r] - inc[0] > 2):
                if inc and inc[0] == nums[l]:
                    inc.popleft()
                if dec and dec[0] == nums[l]:
                    dec.popleft()

                l += 1
                
            if l <= r:
                res += r - l + 1
            
            while inc and inc[-1] > nums[r]:
                inc.pop()
            inc.append(nums[r])

            while dec and dec[-1] < nums[r]:
                dec.pop()
            dec.append(nums[r])

        return res