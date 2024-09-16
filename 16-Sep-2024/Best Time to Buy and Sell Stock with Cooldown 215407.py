# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        if not n: 
            return 0
        
        s0, s1, s2 = [0] * n, [0] * n, [0] * n 
        
        s0[0] = 0
        s1[0] = -prices[0] 
        s2[0] = 0 # dummy
        
        for i in range(1, n):
            s0[i] = max(s0[i-1], s2[i-1])
            s1[i] = max(s1[i-1], s0[i-1] - prices[i])
            s2[i] = s1[i-1] + prices[i]
        
        return max(s0[-1], s2[-1])