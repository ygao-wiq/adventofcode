#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        fast_ptr, slow_ptr, prev_ptr = head, head, None
        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            prev_ptr = slow_ptr
            slow_ptr = slow_ptr.next
        root = TreeNode(slow_ptr.val)
        if prev_ptr:
            prev_ptr.next = None
        root.left = self.sortedListToBST(head) if head != slow_ptr else None
        root.right = self.sortedListToBST(slow_ptr.next)
        return root
# @lc code=end

