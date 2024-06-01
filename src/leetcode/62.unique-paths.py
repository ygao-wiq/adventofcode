#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ret = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    ret[i][j] = 1
                elif j == n-1:
                    ret[i][j] = ret[i+1][j]
                elif i == m-1:
                    ret[i][j] = ret[i][j+1]
                else:
                    ret[i][j] = ret[i][j+1] + ret[i+1][j]
        return ret[0][0]
        
# @lc code=end

