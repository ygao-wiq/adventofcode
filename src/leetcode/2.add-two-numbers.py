# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = ListNode(-1, None)
        curr = head
        while l1 or l2:
            if l1:
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
                l2 = l2.next
            else:
                l2_val = 0
            curr.next = ListNode((l1_val + l2_val + carry)%10, None)
            carry = (l1_val + l2_val + carry) // 10
            curr = curr.next
        if carry:
            curr.next = ListNode(carry, None)
        return head.next