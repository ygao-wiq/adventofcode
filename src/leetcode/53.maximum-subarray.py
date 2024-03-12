#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            current = max(nums[i], current+nums[i])
            max_sum = max(max_sum, current)
        return max_sum
# @lc code=end

