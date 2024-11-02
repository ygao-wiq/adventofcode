#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        red_ptr = -1
        blue_ptr = len(nums)
        while i < blue_ptr:
            if nums[i] == 1:
                i += 1
                continue
            elif nums[i] == 0:
                red_ptr += 1
                temp = nums[i]
                nums[i] = nums[red_ptr]
                nums[red_ptr] = temp
                i += 1
            else:
                blue_ptr -= 1
                temp = nums[i]
                nums[i] = nums[blue_ptr]
                nums[blue_ptr] = temp

# @lc code=end

