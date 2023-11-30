class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        checked = dict()
        for idx, num in enumerate(nums):
            if (target - num) in checked:
                return [checked[target-num], idx]
            checked[num] = idx
        return [-1, -1] 