#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from typing import Optional
    def inorder_backtrack(self, root: Optional[TreeNode], res: list[int]) -> None:
        if root is None:
            return
        self.inorder_backtrack(root.left, res)
        res.append(root.val)
        self.inorder_backtrack(root.right, res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        ans = []
        self.inorder_backtrack(root, ans)
        return ans
        
# @lc code=end

