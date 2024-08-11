#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOneAnother(self, digits: list[int]) -> list[int]:
        if not digits:
            return digits
        n = len(digits) - 1
        digits[len(digits) - 1] = digits[len(digits) - 1]+1
        carry = 0
        if digits[len(digits) - 1] > 9:
            carry = 1
            digits[len(digits) - 1] = 0
        i = len(digits) - 2
        while i>=0 and carry>0:
            temp = digits[i]+1
            carry = temp // 10
            digits[i] = temp % 10
            i -= 1
        if carry>0:
            digits.insert(0, carry)
        return digits
    
    def plusOne(self, digits: list[int]) -> list[int]:
        if not digits:
            return digits
        n = len(digits) - 1
        while n>=0:
            if digits[n] < 9:
                digits[n] += 1
                return digits
            digits[n] = 0
            n -= 1
        ret = [0 for i in range(len(digits)+1)]
        ret[0] = 1
        return ret


        
# @lc code=end

if __name__ == "__main__":
    print(Solution().plusOne([9,9]))