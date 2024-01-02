# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy_head = ListNode(-1, head)
        temp = head
        i = 0
        while temp and i<n:
            temp = temp.next
            i += 1
        to_be_removed = temp
        prev = dummy_head
        curr = prev.next
        while temp:
            prev = curr
            curr = curr.next
            temp = temp.next
        prev.next = curr.next
        return dummy_head.next

if __name__ == "__main__":
    dummy_head = ListNode(-1, None)
    curr = dummy_head
    # for e in [1,2,3,4,5]:
    #     curr.next = ListNode(e, None)
    #     curr = curr.next
    # new_head = Solution().removeNthFromEnd(dummy_head.next, 2)
    # dummy_head = ListNode(-1, None)
    # curr = dummy_head
    # for e in [1]:
    #     curr.next = ListNode(e, None)
    #     curr = curr.next
    # new_head = Solution().removeNthFromEnd(dummy_head.next, 1)
    # dummy_head = ListNode(-1, None)
    # curr = dummy_head