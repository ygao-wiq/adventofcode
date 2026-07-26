#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    post_order_index = -1
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if self.post_order_index == -1:
            self.post_order_index = len(postorder) - 1
        if not inorder or not postorder:
            return None
        val = postorder[self.post_order_index]
        root = TreeNode(val)
        self.post_order_index -= 1
        inorder_index = inorder.index(val)
        root.right = self.buildTree(inorder[inorder_index + 1:], postorder)
        root.left = self.buildTree(inorder[:inorder_index], postorder)
        return root

        
# @lc code=end

