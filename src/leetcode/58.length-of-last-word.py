#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        while i>=0 and s[i] == " ":
            i -= 1
        end_of_last_word = i
        while i>=0 and s[i] != " ":
            i -= 1
        start_of_last_word = i+1
        return end_of_last_word - start_of_last_word + 1

        
# @lc code=end

if __name__ == "__main__":
    print(Solution().lengthOfLastWord("Hello World"))