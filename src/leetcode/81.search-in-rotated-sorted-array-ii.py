#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[start]:
                start += 1
                continue
            pivotInFirst = nums[start]<=nums[mid]
            targetInFirst = nums[start]<=target
            if pivotInFirst ^ targetInFirst:
                if targetInFirst:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return False
# @lc code=end

