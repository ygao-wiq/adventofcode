#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        sign = (dividend<0) ^ (divisor<0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while divisor <= dividend:
            temp_divisor = divisor
            i = 1
            while temp_divisor <= dividend:
                temp_divisor <<= 1
                i <<= 1
            if i == 1:
                dividend -= temp_divisor
                quotient += 1
            else:
                dividend -= (temp_divisor>>1)
                quotient += i>>1
        return -quotient if sign else quotient

# @lc code=end
if __name__ == "__main__":
    print(Solution().divide(7, -3))
    print(Solution().divide(2147483647, 1))
