#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
class Solution:

    def __init__(self):
        self.wordCount: dict[str, int] = dict()
        self.wordLength: int = 0
        self.substringSize: int = 0
        self.k = 0
        self.n = 0
    def slideWindow(self, left: int, s: str, answer: list[int]):
        wordsFound: dict[str, int] = dict()
        wordsUsed = 0
        excessWord = False

        right = left
        while right <= self.n - self.wordLength:
            sub = s[right:right+self.wordLength]
            if sub not in self.wordCount:
                wordsFound.clear()
                wordsUsed = 0
                excessWord = False
                left = right + self.wordLength
            else:
                while right - left == self.substringSize or excessWord:
                    leftmostWord = s[left:left + self.wordLength]
                    left += self.wordLength
                    wordsFound[leftmostWord] = wordsFound.get(leftmostWord) - 1
                    if wordsFound.get(leftmostWord) >= self.wordCount.get(leftmostWord):
                        excessWord = False
                    else:
                        wordsUsed -= 1
                wordsFound[sub] = wordsFound.get(sub, 0) + 1
                if wordsFound.get(sub) <= self.wordCount.get(sub):
                    wordsUsed += 1
                else:
                    excessWord = True

                if wordsUsed == self.k and not excessWord:
                    answer.append(left)
            right += self.wordLength


    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        self.wordCount.clear()
        self.n = len(s)
        self.k = len(words)
        self.wordLength = len(words[0])
        self.substringSize = self.wordLength * self.k

        for word in words:
            self.wordCount[word] = self.wordCount.get(word, 0) + 1
        answer: list[int] = list()
        i = 0
        while i<self.wordLength:
            self.slideWindow(i, s, answer)
            i += 1
        return answer
# @lc code=end

if __name__ == "__main__":
    print(Solution().findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))