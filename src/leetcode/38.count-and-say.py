#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n-1)
        count = 0
        prev = -1
        result = []
        for c in s:
            if c == prev:
                count += 1
            else:
                if prev != -1:
                    result.append(f"{count}{prev}")
                prev = c
                count = 1
        result.append(f"{count}{prev}")
        return "".join(result)
        
# @lc code=end

if __name__ == "__main__":
    print(Solution().countAndSay(30))
