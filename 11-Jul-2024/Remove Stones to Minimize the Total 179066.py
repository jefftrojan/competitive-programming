# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

from heapq import heapify, heapreplace

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-p for p in piles]
        heapify(piles)
        for _ in range(k):
            heapreplace(piles, piles[0]//2)

        return -sum(piles)