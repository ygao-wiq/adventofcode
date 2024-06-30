#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
class Solution:
    def format_line(self, line_words: list[str], line_length: int, max_width: int, last_line: bool) -> str:
        word_count = len(line_words)
        space_count = (max_width-line_length) if word_count==1 else (max_width-line_length) // (word_count-1)
        space_remainder = 0 if word_count==1 else (max_width-line_length) % (word_count-1)
        str_builder = []
        if last_line:
            space_remainder = 0
            space_count = 1
        for i, word in enumerate(line_words):
            str_builder.extend(word)
            if space_remainder > 0:
                str_builder.append(" ")
                space_remainder -= 1
            str_builder.extend(" "*space_count if i<word_count and len(str_builder)<max_width else "")
        str_builder.extend(" "*(max_width-len(str_builder)))
        return "".join(str_builder)

    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        line_length = 0
        ans = []
        line_words = []

        for word in words:
            l = line_length + len(word) + len(line_words) - 1
            if l >= maxWidth:
                ans.append(self.format_line(line_words, line_length, maxWidth, False))
                line_length = 0
                line_words.clear()
            line_words.append(word)
            line_length += len(word)
        ans.append(self.format_line(line_words, line_length, maxWidth, True))
        return ans
        
        
# @lc code=end

if __name__ == "__main__":
    print(Solution().fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))