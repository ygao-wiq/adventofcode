#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def transpose(self, matrix: list[list[int]]) -> None:
        for i in range(0, len(matrix)):
            for j in range(i+1, len(matrix[i])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
    def mirror(self, matrix: list[list[int]]) -> None:
        for r in matrix:
            left = 0
            right = len(r) - 1
            while left < right:
                temp = r[left]
                r[left] = r[right]
                r[right] = temp
                left += 1
                right -= 1


    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix=matrix)
        self.mirror(matrix=matrix)
        
# @lc code=end

