# Problem: Best Time to Buy and Sell Stock II - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold = [-1 * prices[i] for i in range(n)]
        sell = [hold[i] + prices[i+1] for i in range(n-1)]
        maxProfit = 0
        for j in range(len(sell)):
            if sell[j] > 0:
                maxProfit += sell[j] 
        return maxProfit