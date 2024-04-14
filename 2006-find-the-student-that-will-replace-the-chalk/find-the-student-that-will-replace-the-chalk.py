class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        pref = [0]
        for c in chalk:
            pref.append(pref[-1] + c)

        k %= pref[-1]
        left, right = 0, len(chalk) - 1
        while left <= right:
            m = (left + right) >> 1
            if pref[m + 1] > k:
                right = m - 1
            else:
                left = m + 1
        return left