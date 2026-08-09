#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: TreeNode | None, targetSum: int, current_path: list[int], result: list[list[int]]) -> None:
        current_path.append(root.val)
        if not root.left and not root.right and root.val == targetSum:
            result.append(current_path[:])
        else:
            if root.left:
                self.dfs(root.left, targetSum - root.val, current_path, result)
            if root.right: 
                self.dfs(root.right, targetSum - root.val, current_path, result)
        current_path.pop()
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        result: list[list[int]] = []
        if not root:
            return result
        self.dfs(root, targetSum, [], result)
        return result

# @lc code=end

