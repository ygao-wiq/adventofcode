#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        last_pos = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i+nums[i] >= last_pos:
                last_pos = i
        return last_pos == 0
        
# @lc code=end

