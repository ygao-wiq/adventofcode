#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0 or len(t) == 0:
            return ""
        dict_char_found_count = {}
        for c in t:
            dict_char_found_count[c] = dict_char_found_count.get(c, 0) + 1
        
        required_nunique_chars = len(dict_char_found_count)
        filtered_string = []
        for i, c in enumerate(s):
            if c in dict_char_found_count:
                filtered_string.append((i, c))
        l = 0
        r = 0
        found = 0
        window_counts = {}
        ans = [-1, l, r]
        while r < len(filtered_string):
            c = filtered_string[r][1]
            window_counts[c] = window_counts.get(c, 0) + 1
            if c in dict_char_found_count and window_counts.get(c) == dict_char_found_count.get(c):
                found += 1
            while l<=r and found == required_nunique_chars:
                c1 = filtered_string[l][1]
                end = filtered_string[r][0]
                start = filtered_string[l][0]
                if ans[0] == -1 or end-start+1 < ans[0]:
                    ans[0] = end-start+1
                    ans[1] = start
                    ans[2] = end
                window_counts[c1] = window_counts.get(c1) - 1
                if c1 in dict_char_found_count and window_counts.get(c1) < dict_char_found_count.get(c1):
                    found -= 1
                l += 1
            r +=1
        return "" if ans[0]==-1 else s[ans[1]:ans[2]+1]
# @lc code=end

if __name__ == "__main__":
    print(Solution().minWindow("cabwefgewcwaefgcf", "cae"))
    print(Solution().minWindow("ADOBECODEBANC", "ABC"))
    print(Solution().minWindow("a", "a"))
    print(Solution().minWindow("a", "aa"))