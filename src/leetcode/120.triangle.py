#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        depth = len(triangle)
        dp = [triangle[0][0]]
        ret = dp[0]
        for i in range(1, depth):
            prev_dp = dp
            dp = [0] * (i + 1)
            for j in range(i+1):
                if j == 0:
                    dp[j] = prev_dp[j] + triangle[i][j]
                elif j == i:
                    dp[j] = prev_dp[j-1] + triangle[i][j]
                else:
                    dp[j] = min(prev_dp[j-1], prev_dp[j]) + triangle[i][j]
            ret = min(dp)
        return ret
        
# @lc code=end

