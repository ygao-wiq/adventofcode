#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def convert_to_int(self, c: str) -> int:
        return ord(c) - 48

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        if num1 == "1":
            return num2
        if num2 == "1":
            return num1
        
        if len(num1) <= len(num2):
            multiplier = num1
            multiplicand = num2
        else:
            multiplier = num2
            multiplicand = num1
        
        ret = 0
        for m1 in multiplier:
            temp = 0
            carry = 0
            decimal = 1
            mn1 = self.convert_to_int(m1)
            for m2 in multiplicand:
                mn2 = self.convert_to_int(m2)
                temp = temp * 10 + mn1 * mn2
            ret = ret * 10 + temp
        return str(ret)



# @lc code=end
if __name__ == "__main__":
    print(Solution().multiply("123", "456"))
