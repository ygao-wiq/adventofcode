#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        start = 0
        cols = len(matrix[0])
        rows = len(matrix)
        end = cols*rows-1

        while start <= end:
            mid = start + (end-start) // 2
            mid_row = mid // cols
            mid_col = mid % cols
            curr = matrix[mid_row][mid_col]
            if curr == target:
                return True
            elif curr < target:
                start = mid + 1
            else:
                end = mid - 1
        return False
        
# @lc code=end
if __name__ == "__main__":
    print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
