#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        f1 = 1
        f2 = 2
        if n == 1:
            return f1
        if n == 2:
            return f2
        i = 3
        while i<=n:
            ans = f1 + f2
            f1 = f2
            f2 = ans
            i += 1
        return ans

# @lc code=end