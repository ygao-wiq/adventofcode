#
# @lc app=leetcode id=52 lang=python3
#
#

# @lc code=start
class Solution:    
    def backtrace(self, col_sets: set[int], diag_sets: set[int], anti_diag_sets: set[int], row: int, size: int) -> int:
        if row == size:
            return 1
        solution = 0
        for col in range(size):
            diagonal = row - col
            anti_diagonal = row + col
            if col in col_sets or diagonal in diag_sets or anti_diagonal in anti_diag_sets:
                continue
            col_sets.add(col)
            diag_sets.add(diagonal)
            anti_diag_sets.add(anti_diagonal)
            solution += self.backtrace(col_sets, diag_sets, anti_diag_sets, row+1, size)
            col_sets.remove(col)
            diag_sets.remove(diagonal)
            anti_diag_sets.remove(anti_diagonal)
        return solution
    def totalNQueens(self, n: int) -> int:
        return self.backtrace(set(), set(), set(), 0, n)