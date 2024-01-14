#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def computePrefix(self, needle: str) -> list[int]:
        ret = [0 for _ in range(len(needle))]
        ret[0] = -1
        k = -1
        i = 1
        while i < len(needle):
            while k>=0 and needle[k+1] != needle[i]:
                k = ret[k]
            if needle[k+1] == needle[i]:
                k = k + 1
            ret[i] = k
            i += 1
        return ret
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        if not needle:
            return 0
        if not haystack:
            return -1
        find = -1
        prefix = self.computePrefix(needle=needle)
        k = -1
        i = 0
        while i <len(haystack):
            while k>=0 and haystack[i] != needle[k+1]:
                k = prefix[k]
            if needle[k+1] == haystack[i]:
                k = k + 1
            if k == len(needle)-1:
                return i-len(needle)+1
            i += 1
        return -1
        
# @lc code=end
if __name__ == "__main__":
    print(Solution().strStr("sadbutsad", "sad"))
    print(Solution().strStr("aaa", "aaa"))
