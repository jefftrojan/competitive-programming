class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = 2**n-1
        invert = 0
        while length !=1:
            mid = (length+1)//2
            if k <mid:
                pass
            elif k>mid:
                invert= abs(1-invert)
                k = 2*mid-k
            else:
                return '1' if invert==0 else '0'
            length = mid-1
        return '0' if invert == 0 else '1'
            