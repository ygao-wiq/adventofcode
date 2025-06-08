#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> list[int]:
        i = 0
        count = 1 << n
        ans = []
        while i < count:
            ans.append(i ^ (i >> 1))
            i += 1
        return ans
            
        
# @lc code=end

