#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []

        def backtrack(ans, nums, current, subset_length, start):
            current_length = len(current)
            if current_length == subset_length:
                ans.append(current.copy())
                return
            i = start
            while i < len(nums):
                current.append(nums[i])
                backtrack(ans, nums, current, subset_length, i+1)
                current.pop()
                while i<len(nums)-1 and nums[i] == nums[i+1]:
                    i += 1
                i += 1

        for i in range(len(nums)+1):
            backtrack(ans, nums, [], i, 0)
        return ans
        
# @lc code=end
if __name__ == "__main__":
    input = [1, 2, 2]
    solution = Solution()
    output = solution.subsetsWithDup(input)
    print(output)  # Expected: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
