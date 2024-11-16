#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        nums = [i+1 for i in range(k)]
        nums.append(n+1)
        ans = []
        i = 0
        while i<k:
            ans.append(nums[0:k])
            i = 0
            while i<k and nums[i+1]==nums[i]+1:
                nums[i] = i + 1
                i += 1
            nums[i] = nums[i] + 1
        return ans

        
# @lc code=end

if __name__ == "__main__":
    print(Solution().combine(4, 2))