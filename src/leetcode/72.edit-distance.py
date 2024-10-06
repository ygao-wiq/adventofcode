#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_1 = len(word1)
        len_2 = len(word2)
        if len_1 * len_2 == 0:
            return len_1 + len_2
        dp = [[i if j==0 else (j if i==0 else 0) for j in range(len_2+1)] for i in range(len_1+1)]

        for i in range(1, len_1+1):
            for j in range(1, len_2+1):
                left = dp[i - 1][j] + 1
                down = dp[i][j - 1] + 1
                left_down = dp[i - 1][j - 1] + 1
                if word1[i-1] == word2[j-1]:
                    left_down -= 1
                dp[i][j] = min(left, min(down, left_down))
        return dp[len_1][len_2]
        
# @lc code=end

if __name__ == "__main__":
    print(Solution().minDistance("abc", "def"))