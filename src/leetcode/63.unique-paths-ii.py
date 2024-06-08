#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        ret = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    ret[i][j] = 0
                elif i == m-1 and j == n-1:
                    ret[i][j] = 1
                elif j == n-1:
                    ret[i][j] = ret[i+1][j]
                elif i == m-1:
                    ret[i][j] = ret[i][j+1]
                else:
                    ret[i][j] = ret[i][j+1] + ret[i+1][j]
        return ret[0][0]

# @lc code=end

