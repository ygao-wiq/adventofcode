#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        lqueue = [root]
        rqueue = [root]
        while lqueue and rqueue:
            if len(lqueue) != len(rqueue):
                return False
            for _ in range(len(lqueue)):
                lnode = lqueue.pop(0)
                rnode = rqueue.pop(0)
                if not lnode and not rnode:
                    continue
                if not lnode or not rnode:
                    return False
                if lnode.val != rnode.val:
                    return False
                lqueue.append(lnode.left)
                lqueue.append(lnode.right)
                rqueue.append(rnode.right)
                rqueue.append(rnode.left)

        return True
        
# @lc code=end

