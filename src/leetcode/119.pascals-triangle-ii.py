#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            row = [1, 1]
            for i in range(2, rowIndex + 1):
                new_row = [1] * (i + 1)
                for j in range(1, i):
                    new_row[j] = row[j - 1] + row[j]
                row = new_row
            return row
        
# @lc code=end

