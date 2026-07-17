#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        ans = []
        level = 0
        if root:
            queue.append(root)
        while queue:
            queue_size = len(queue)
            level += 1
            if len(ans) < level:
                ans.append([])
            level_list = ans[-1]
            for _ in range(queue_size):
                curr = queue.pop(0)
                level_list.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return ans
# @lc code=end

