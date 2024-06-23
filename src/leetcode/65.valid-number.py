#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:

        dfa_maps = [
            {"digit": 1, "sign": 2, "dot": 3},
            {"digit": 1, "dot": 4, "exponent": 5},
            {"digit": 1, "dot": 3},
            {"digit": 4},
            {"digit": 4, "exponent": 5},
            {"sign": 6, "digit": 7},
            {"digit": 7},
            {"digit": 7},
        ]
        acceptable_dfa_states = {1, 4, 7}
        current_dfa_state = 0
        group = ""

        for c in s:
            if c.isdigit():
                group = "digit"
            elif c == "+" or c == "-":
                group = "sign"
            elif c == "e" or c == "E":
                group = "exponent"
            elif c == ".":
                group = "dot"
            else:
                return False
            if group not in dfa_maps[current_dfa_state]:
                return False
            current_dfa_state = dfa_maps[current_dfa_state][group]
        return current_dfa_state in acceptable_dfa_states
# @lc code=end

