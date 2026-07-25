#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    preorder_index = 0
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[self.preorder_index])
        self.preorder_index += 1
        if len(inorder) == 1:
            return root
        inorder_index = inorder.index(root.val)
        left_node = self.buildTree(preorder, inorder[0:inorder_index])
        right_node = self.buildTree(preorder, inorder[inorder_index+1:])
        root.left, root.right = left_node, right_node
        return root
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    # r = s.buildTree([3,9,20,15,7], [9,3,15,20,7])
    # r = s.buildTree([1,2,3], [3,2,1])
    # r = s.buildTree([1,2], [1,2])
    # r = s.buildTree([3,1,2,4], [1,2,3,4])
    print("Done")
