class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_idx_map = dict()
        i = j = 0
        max_length = 0
        str_length = len(s)

        while j < str_length:
            if s[j] in char_idx_map:
                i = max(i, char_idx_map[s[j]])
            char_idx_map[s[j]] = j+1
            max_length = max(max_length, j-i+1)
            j = j+1
        return max_length
