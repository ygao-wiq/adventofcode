#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        rows = len(matrix)
        columns = len(matrix[0])
        up = 0
        left = 0
        right = columns - 1
        down = rows - 1
        results = []

        while len(results) < rows*columns:
            for col in range(left, right+1, 1):
                results.append(matrix[up][col])
            
            for row in range(up+1, down, 1):
                results.append(matrix[row][right])
            
            if up != down:
                for col in range(right, left-1, -1):
                    results.append(matrix[down][col])
            if left != right:
                for row in range(down-1, up, -1):
                    results.append(matrix[row][left])
            left += 1
            right -= 1
            up += 1
            down -= 1
        return results
        
# @lc code=end
if __name__ == "__main__":
    print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
