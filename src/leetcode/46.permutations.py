#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def swap(self, nums, i, k) -> None:
        nums[i], nums[k] = nums[k], nums[i]

    def backtrace(self, nums: list[int], ret: list[list], start: int):
        if start == len(nums):
            ret.append(nums.copy())
        i = start
        while i<len(nums):
            self.swap(nums, start, i)
            self.backtrace(nums, ret, start+1)
            self.swap(nums, start, i)
            i += 1


    def permute(self, nums: list[int]) -> list[list[int]]:
        ret = list()
        self.backtrace(nums, ret, 0)
        return ret

# @lc code=end
if __name__ == "__main__":
    print(Solution().permute([1,2,3]))
