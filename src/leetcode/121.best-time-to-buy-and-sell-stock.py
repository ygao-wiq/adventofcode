#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_by_day = [-1] * len(prices)
        max_profit = 0
        max_by_day[-1] = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            max_by_day[i] = max(prices[i], max_by_day[i+1])
        
        for i in range(len(prices)):
            max_profit = max(max_profit, max_by_day[i] - prices[i])
        
        return max_profit
        
# @lc code=end

