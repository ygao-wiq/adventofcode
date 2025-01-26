#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        cnt = 1
        k = 0
        for idx in range(1, len(nums)):
            if nums[idx] == nums[idx-1] and cnt < 2:
                k += 1
                nums[k] = nums[idx]
                cnt += 1
            elif nums[idx] != nums[idx-1]:
                k += 1
                nums[k] = nums[idx]
                cnt = 1
        return k+1
        
# @lc code=end

