#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:

        n = len(nums)
        has_one = False
        for i in nums:
            if i == 1:
                has_one = True
                break
        if not has_one:
            return 1
        
        for i, j in enumerate(nums):
            if j<=0 or j>n:
                nums[i] = 1
        
        for i, j in enumerate(nums):
            temp = abs(j)
            if temp == n:
                nums[0] = -1 * abs(nums[0])
            else:
                nums[temp] = -1 * abs(nums[temp])
        
        i = 1
        while i<n:
            if nums[i]>0:
                return i
            i += 1
        if nums[0] > 0:
            return n
        return n+1

        
# @lc code=end

if __name__ == "__main__":
    print(Solution().firstMissingPositive([1,2,6,3,5,4]))