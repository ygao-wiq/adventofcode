#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTreesHelper(self, start, end, cache: dict) -> list[Optional[TreeNode]]:
        if start > end:
            return [None]
        ans = []
        if (start, end) in cache:
            return cache[(start, end)]
        for i in range(start, end + 1):
            left_trees = self.generateTreesHelper(start, i - 1, cache)
            cache[(start, i - 1)] = left_trees
            right_trees = self.generateTreesHelper(i + 1, end, cache)
            cache[(i + 1, end)] = right_trees
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    ans.append(root)
        return ans
    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        if n == 0:
            return []
        return self.generateTreesHelper(1, n, dict())
# @lc code=end

