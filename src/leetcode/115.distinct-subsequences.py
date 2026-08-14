#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = 1
        mem = {}
        for i in range(len(s)):
            dp[i+1][0] = 1
            char_map = mem.get(s[i], {})
            char_map[i] = 1
            mem[s[i]] = char_map
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if j > i:
                    dp[i][j] = 0
                if t[j-1] not in mem:
                    dp[i][j] = 0
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[len(s)][len(t)]
        
# @lc code=end

