#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
from collections import deque
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        valid_mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = list()
        for c in s:
            if c in valid_mapping and len(stack)>0:
                if stack[-1] == valid_mapping[c]:
                    stack.pop()
                else:
                    return False
            elif c in ["(", "{", "["]:
                stack.append(c)
            else:
                return False
        return len(stack) == 0
# @lc code=end

