class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        middle = len(strs) // 2
        lcp_left = self.longestCommonPrefix(strs[:middle])
        lcp_right = self.longestCommonPrefix(strs[middle:])
        i = 0
        while i<min(len(lcp_left), len(lcp_right)):
            if lcp_left[i] != lcp_right[i]:
                break
            i += 1
        return lcp_left[:i]
    
if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))
    print(Solution().longestCommonPrefix(["dog","racecar","car"]))