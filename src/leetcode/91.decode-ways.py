#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        if s and s[0] != '0':
            dp[1] = 1
        for i in range(2, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1] if s else 0
# @lc code=end

