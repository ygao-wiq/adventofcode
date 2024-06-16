#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ret = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    ret[i][j] = grid[i][j]
                elif j == n-1:
                    ret[i][j] = grid[i][j] + ret[i+1][j]
                elif i == m-1:
                    ret[i][j] = grid[i][j] + ret[i][j+1]
                else:
                    ret[i][j] = min(ret[i][j+1], ret[i+1][j]) + grid[i][j]
        return ret[0][0]
# @lc code=end

