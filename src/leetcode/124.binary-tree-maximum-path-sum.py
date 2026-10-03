#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# [-10,9,20,null,null,15,7]
# [1, -2, -3, 1, 3, -2, null, -1]
import sys
class Solution:
    max_sum = sys.maxsize * -1
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.getMaxSum(root)
        return self.max_sum

    def getMaxSum(self, root: TreeNode | None) -> int:
        if not root:
            return sys.maxsize * -1
        left_max = self.getMaxSum(root.left)
        right_max = self.getMaxSum(root.right)
        sub_max = max(left_max, right_max)
        self.max_sum = max(self.max_sum, root.val, sub_max, root.val + sub_max, root.val + left_max + right_max)
        return max(root.val, root.val + sub_max)
        
# @lc code=end

