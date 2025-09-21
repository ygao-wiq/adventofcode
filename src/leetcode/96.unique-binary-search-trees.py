#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def countTrees(self, start, end, cache) -> int:
        if start > end:
            return 1
        if (start, end) in cache:
            return cache[(start, end)]
        ans = 0
        for i in range(start, end + 1):
            left = self.countTrees(start, i - 1, cache)
            cache[(start, i - 1)] = left
            right = self.countTrees(i + 1, end, cache)
            cache[(i + 1, end)] = right
            ans += left * right
        cache[(start, end)] = ans
        return ans

    def numTrees3(self, n: int) -> int:
        if n == 0:
            return 0
        return self.countTrees(1, n, dict())
    
    def numTrees2(self, n: int) -> int:
        if n == 0:
            return 0
        ans = [0] * (n + 1)
        ans[0] = 1
        ans[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                ans[i] += ans[j-1] * ans[i-j]
        return ans[n]
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        count = 1
        for i in range(2, n+1):
            count = count * 2 * (2 * i - 1) // (i + 1)
        return count

# @lc code=end

