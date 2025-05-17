#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if len(matrix) == 0:
            return 0
        maxarea = 0
        dp = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    # compute the maximum width and update dp with it
                    dp[i][j] = 1 if j == 0 else dp[i][j-1] + 1

                    width = dp[i][j]

                    # compute the maximum area rectangle with a lower right corner at [i, j]
                    k = i
                    while k >= 0:
                        width = min(width, dp[k][j])
                        maxarea = max(maxarea, width * (i - k + 1))
                        k -= 1
        return maxarea
# @lc code=end

