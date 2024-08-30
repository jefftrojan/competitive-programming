# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        ans = list(str(bin(n)[2:]))
        for i in range(len(ans)- 1) :
            if ans[i] == ans[i + 1] :
                return False
                
        return True