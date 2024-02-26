#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sLen = len(s)
        pLen = len(p)
        sIdx = 0
        pIdx = 0
        starIdx = -1 
        sTmpIdx = -1

        while (sIdx < sLen):
            if (pIdx < pLen and (p[pIdx] == '?' or p[pIdx] == s[sIdx])):
                sIdx += 1
                pIdx += 1
            elif (pIdx < pLen and p[pIdx] == '*'):
                starIdx = pIdx
                sTmpIdx = sIdx
                pIdx += 1
            elif (starIdx == -1):
                return False
            else:
                pIdx = starIdx + 1
                sIdx = sTmpIdx + 1
                sTmpIdx = sIdx
        i = pIdx
        while i < pLen:
            if (p[i] != '*'):
                return False
            i += 1
        return True
        
# @lc code=end

