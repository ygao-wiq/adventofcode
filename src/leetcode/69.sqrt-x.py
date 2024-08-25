#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        ans = 1.0
        x0 = x
        while abs(ans - x0) >= 1:
            x0 = ans
            ans = x0/2 + x/2/x0
        return int(ans)
        
# @lc code=end

if __name__ == "__main__":
    print(Solution().mySqrt(9))
