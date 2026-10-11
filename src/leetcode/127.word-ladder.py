#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        ans = 0
        words = set(wordList)
        if endWord not in words:
            return 0
        words.discard(beginWord)
        from collections import deque
        q = deque([(beginWord, 1)])
        while q:
            word, step = q.popleft()
            if word == endWord:
                return step
            s = list(word)
            for i in range(len(s)):
                ch = s[i]
                for j in range(26):
                    s[i] = chr(ord('a') + j)
                    t = ''.join(s)
                    if t in words:
                        words.discard(t)
                        q.append((t, step + 1))
                s[i] = ch
        return 0
        
# @lc code=end

