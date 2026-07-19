#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        q = []
        q.append(root)
        level = 0
        while q:
            level += 1
            curr = []
            t_q = q[:]
            q_sz = len(t_q)
            q.clear()
            for _ in range(q_sz):
                node = t_q.pop(0)
                curr.append(node.val)
                if level % 2 == 1:
                    if node.left:
                        q.insert(0, node.left)
                    if node.right:
                        q.insert(0, node.right)
                else:
                    if node.right:
                        q.insert(0, node.right)
                    if node.left:
                        q.insert(0, node.left)
            ans.append(curr)
        return ans
    
        
# @lc code=end

