#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1, None)
        dummy_head.next = head
        current = dummy_head
        while head and head.next:
            first = head
            second = head.next
            current.next = second
            first.next = second.next
            second.next = first
            current = first
            head = first.next
        return dummy_head.next
        
# @lc code=end

