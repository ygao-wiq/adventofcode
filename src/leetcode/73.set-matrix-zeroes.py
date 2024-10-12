#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        is_col_mode = False
        i = 0
        while i<R:
            if matrix[i][0] == 0:
                is_col_mode = True
            j = 1
            while j<C:
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                j += 1
            i +=1
        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(1, C):
                matrix[0][j] = 0
        if is_col_mode:
            for i in range(0, R):
                matrix[i][0] = 0
        
# @lc code=end
if __name__ == "__main__":
    input_mat = [[1],[0]]
    Solution().setZeroes(input_mat)
    print(input_mat)
