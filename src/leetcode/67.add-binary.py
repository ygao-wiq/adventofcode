#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ret = []
        len_a = len(a)
        len_b = len(b)
        carry = 0
        while len_a>0 or len_b>0:
            num_a = int(a[len_a-1]) if len_a>0 else 0
            num_b = int(b[len_b-1]) if len_b>0 else 0
            sum = num_a + num_b + carry
            carry = sum // 2
            ret.insert(0, str(sum % 2))
            len_a -= 1
            len_b -= 1

        if carry > 0:
            ret.insert(0, str(carry))
        return "".join(ret)

        
# @lc code=end

if __name__ == "__main__":
    print(Solution().addBinary("1010", "1011"))