#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if target == nums[mid]:
                return mid
            elif nums[mid] >= nums[left]:
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
# @lc code=end

