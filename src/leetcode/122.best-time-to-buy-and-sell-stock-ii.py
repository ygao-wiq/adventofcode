#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_min = sys.maxsize
        profit = 0
        prev = None
        for price in prices:
            if prev is None:
                prev = price
                prev_min = price
                continue
            if price < prev:
                profit += (prev - prev_min)
                prev_min = price
            prev = price

        if prev is not None and prev > prev_min:
            profit += (prev - prev_min)
        return profit
# @lc code=end

