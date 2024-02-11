#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_validity = [set() for _ in range(9)]
        column_validity = [set() for _ in range(9)]
        block_validity = [set() for _ in range(9)]
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c == ".":
                    continue
                if c in row_validity[i]:
                    return False
                row_validity[i].add(c)
                if c in column_validity[j]:
                    return False
                column_validity[j].add(c)
                if c in block_validity[i // 3 * 3 + j // 3]:
                    return False
                block_validity[i // 3 * 3 + j // 3].add(c)
        return True
# @lc code=end

