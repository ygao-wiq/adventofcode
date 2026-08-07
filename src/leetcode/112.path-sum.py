#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return (root.left is not None and self.hasPathSum(root.left, targetSum - root.val)) or (root.right is not None and self.hasPathSum(root.right, targetSum - root.val))
    
if __name__ == "__main__":
    sol = Solution()
    # Example test case
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = None
    targetSum = 0
    print(sol.hasPathSum(root, targetSum))  # Output: True
# @lc code=end

