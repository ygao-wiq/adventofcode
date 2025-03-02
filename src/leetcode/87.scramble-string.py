#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#

# @lc code=start
class Solution:
    memory = dict()
    def _isScramble(self, s1: str, s2: str) -> bool:
        key = s1 + " " + s2
        if key in self.memory:
            return self.memory[key]
        
        if s1 == s2:
            self.memory[key] = True
            return True

        if len(s1) != len(s2) or len(s1) <= 1 or sorted(s1) != sorted(s2):
            self.memory[key] = False
            return False
        n = len(s1)
        for i in range(1, n):
            if self._isScramble(s1[:i], s2[:i]) and self._isScramble(s1[i:], s2[i:]):
                self.memory[key] = True
                return True
            if self._isScramble(s1[:i], s2[n-i:]) and self._isScramble(s1[i:], s2[:n-i]):
                self.memory[key] = True
                return True
        self.memory[key] = False
        return False

    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        return self._isScramble(s1, s2)
        
# @lc code=end

