#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:

    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                if isFirst:
                    if mid == start or nums[mid-1] != nums[mid]:
                        return mid
                    end = mid -1
                else:
                    if mid == end or nums[mid+1] != nums[mid]:
                        return mid
                    start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.findBound(nums, target, True)
        if first == -1:
            return [-1, -1]
        last = self.findBound(nums, target, False)
        return [first, last]
        
# @lc code=end

