#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        ans = [[0 for i in range(n)] for i in range(n)]
        visited = [[False for i in range(n)] for i in range(n)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        current_direction = 0
        direction_changed = 0
        row = 0
        col = 0
        num = 1
        ans[row][col] = num 
        visited[row][col] = True
        while direction_changed < 2:
            while row+directions[current_direction][0]>=0 and row+directions[current_direction][0]<n and col+directions[current_direction][1]>=0 and col+directions[current_direction][1]<n and not visited[row+directions[current_direction][0]][col+directions[current_direction][1]]:
                row += directions[current_direction][0]
                col += directions[current_direction][1]
                direction_changed = 0
                num += 1
                ans[row][col] = num
                visited[row][col] = True
            current_direction = (current_direction + 1) % len(directions)
            direction_changed += 1
        return ans
        
# @lc code=end

if __name__ == "__main__":
    Solution().generateMatrix(3)