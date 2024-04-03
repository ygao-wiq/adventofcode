#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        N = n
        ans = 1.0
        if N < 0:
            N = -N
            x = 1/x
        current = x
        i = N
        while i>0:
            if i%2 == 1:
                ans *= current
            current *= current
            i //= 2
        return ans
        
# @lc code=end

