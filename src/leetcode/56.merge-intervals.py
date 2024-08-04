#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = []
        for e in intervals:
            if not ans or e[0]>ans[-1][1]:
                ans.append(e)
            elif e[1] > ans[-1][1]:
                ans[-1][1] = e[1]    
        return ans
# @lc code=end

