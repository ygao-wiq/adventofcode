#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        new_start = newInterval[0]
        new_end = newInterval[1]
        ans = []
        i = 0
        while i<len(intervals):
            if intervals[i][0] < new_start:
                ans.append(intervals[i])
                i += 1
            else:
                break
        if i==0 or ans[-1][-1] < new_start:
            ans.append(newInterval)
        else:
            ans[-1][-1] = max(ans[-1][-1], new_end)

        while i<len(intervals):
            if intervals[i][0] > ans[-1][-1]:
                ans.append(intervals[i])
            else:
                ans[-1][-1] = max(intervals[i][1], ans[-1][-1])
            i += 1
        return ans
# @lc code=end

