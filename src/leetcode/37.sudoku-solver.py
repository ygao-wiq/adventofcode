#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution:
    board_size = 9
    def backtrack(self, board: list[list[str]], row: int, col: int) -> bool:
        if row >= self.board_size:
            return True
        c = board[row][col]
        if c == ".":
            remained_set = {"1", "2", "3", "4", "5", "6", "7", "8", "9"} - (self.row_validity[row].union(self.column_validity[col]).union(self.block_validity[row // 3 * 3 + col // 3]))
            for nc in remained_set:
                board[row][col] = nc
                self.row_validity[row].add(nc)
                self.column_validity[col].add(nc)
                self.block_validity[row // 3 * 3 + col // 3].add(nc)
                nn = row * self.board_size + col + 1
                if self.backtrack(board, nn // self.board_size, nn % self.board_size):
                    return True
                board[row][col] = "."
                self.row_validity[row].remove(nc)
                self.column_validity[col].remove(nc)
                self.block_validity[row // 3 * 3 + col // 3].remove(nc)
            return False
        # elif c in self.row_validity[row] or c in self.column_validity[col] or c in self.block_validity[row // 3 * 3 + col // 3]:
        #     return False
        else:
            nn = row * self.board_size + col + 1
            return self.backtrack(board, nn // self.board_size, nn % self.board_size)

    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.row_validity = [set() for _ in range(9)]
        self.column_validity = [set() for _ in range(9)]
        self.block_validity = [set() for _ in range(9)]
        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if board[i][j] != ".":
                    self.row_validity[i].add(c)
                    self.column_validity[j].add(c)
                    self.block_validity[i // 3 * 3 + j // 3].add(c)
        self.backtrack(board, 0, 0)
        
# @lc code=end

if __name__ == "__main__":
    input = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    input = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    Solution().solveSudoku(input)
    print(input)