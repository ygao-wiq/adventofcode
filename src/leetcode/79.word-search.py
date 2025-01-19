#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def backtrace(self, i: int, j: int, word: str, idx: int, rows: int, cols: int, board: list[list[str]]):
        if idx >= len(word):
            return True
        if i < 0 or i == rows or j < 0 or j == cols or board[i][j] != word[idx]:
            return False
        ret = False
        board[i][j] = "#"
        offsets = [(0,1), (1,0), (0, -1), (-1, 0)]
        for offset in offsets:
            if self.backtrace(i+offset[0], j+offset[1], word, idx+1, rows, cols, board):
                ret = True
                break
        board[i][j] = word[idx]
        return ret

    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        for i in range(ROWS):
            for j in range(COLS):
                if (self.backtrace(i, j, word, 0, ROWS, COLS, board)):
                    return True
        return False
        
# @lc code=end

