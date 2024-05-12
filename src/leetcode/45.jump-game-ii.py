import sys
#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        ret = [sys.maxsize for _ in nums]
        ret[n-1] = 0
        i = n-2
        while i>=0:
            if i + nums[i] >= n-1:
                ret[i] = 1
            else:
                temp = [ret[i+k]+1 for k in range(1, nums[i]+1) if i+k < n]
                if temp:
                    ret[i] = min(temp)
            i -= 1
        return ret[0]

# @lc code=end

