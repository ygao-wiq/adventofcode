#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([(root, 1)])  # Queue of (node, depth)
        while q:
            q_sz = len(q)
            for _ in range(q_sz):
                node, depth = q.popleft()
                if not node.left and not node.right:  # Leaf node
                    return depth
                if node.left:
                    q.append((node.left, depth + 1))
                if node.right:
                    q.append((node.right, depth + 1))
        return 0
        
# @lc code=end

