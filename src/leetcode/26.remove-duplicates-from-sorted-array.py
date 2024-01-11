#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        idx = -1
        for i, n in enumerate(nums):
            if n != prev:
                idx += 1
                nums[idx] = n
                prev = n
        return idx+1
        
# @lc code=end

