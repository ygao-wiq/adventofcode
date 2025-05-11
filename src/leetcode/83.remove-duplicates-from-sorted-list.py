#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = None
        prev = dummy_head
        curr = head
        while curr:
            if prev is None:
                dummy_head = curr
                prev = dummy_head
            elif curr.val == prev.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy_head

# @lc code=end

