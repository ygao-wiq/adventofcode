#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head:
            return head
        temp = head
        cnt = 1
        while temp.next:
            temp = temp.next
            cnt += 1
        k = k % cnt
        if k == 0:
            return head
        k = cnt - k
        temp.next = head
        prev = head
        while k>0:
            prev = head
            head = head.next
            k -= 1
        prev.next = None
        return head
        
# @lc code=end

