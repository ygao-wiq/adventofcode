#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        ans.append([])

        for n in nums:
            new_subsets = []
            for curr in ans:
                new_curr = curr.copy()
                new_curr.append(n)
                new_subsets.append(new_curr)
            ans.extend(new_subsets)
        return ans

        
# @lc code=end
if __name__ == "__main__":
    print(Solution().subsets([0,1,2,3]))
