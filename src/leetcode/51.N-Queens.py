#
# @lc app=leetcode id=51 lang=python3
#
#

# @lc code=start
class Solution:
    def createBoard(self, board: list[list[str]]) -> list[str]:
        ret = []
        for row in board:
            ret.append("".join(row))
        return ret
    
    def backtrace(self, ans: list[list[str]], board: list[list[str]], col_sets: set[int], diag_sets: set[int], anti_diag_sets: set[int], row: int, size: int):
        if row == size:
            ans.append(self.createBoard(board=board))
            return
        
        for col in range(size):
            diagonal = row - col
            anti_diagonal = row + col
            if col in col_sets or diagonal in diag_sets or anti_diagonal in anti_diag_sets:
                continue
            board[row][col] = "Q"
            col_sets.add(col)
            diag_sets.add(diagonal)
            anti_diag_sets.add(anti_diagonal)
            self.backtrace(ans, board, col_sets, diag_sets, anti_diag_sets, row+1, size)
            board[row][col] = '.'
            col_sets.remove(col)
            diag_sets.remove(diagonal)
            anti_diag_sets.remove(anti_diagonal)
        


    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        board = [["." for _ in range(n)] for _ in range(n)]
        self.backtrace(ans, board, set(), set(), set(), 0, n)
        return ans

    
if __name__ == "__main__":
    print(Solution().solveNQueens(9))