#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ret = list()
        if n == 0:
            ret.append("")
        else:
            for i in range(n):
                left_combinations = list()
                self.backtrace(list(), 0, 0, left_combinations, i)
                for left in left_combinations:
                    right_combinations = list()
                    self.backtrace(list(), 0, 0, right_combinations, n-1-i)
                    for right in right_combinations:
                        ret.append("(" + left + ")" + right)
        return ret
    
    def backtrace(self, current: list[str], open: int , close: int, combinations: list[str], max: int) -> None:
        if len(current) == 2*max:
            combinations.append("".join(current))
            return combinations
        if open < max:
            current.append("(")
            self.backtrace(current, open+1, close, combinations, max)
            current.pop(-1)
        if close < open:
            current.append(")")
            self.backtrace(current, open, close+1, combinations, max)
            current.pop(-1)

if __name__ == "__main__":
    print(Solution().generateParenthesis(0))

