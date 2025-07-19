#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        prev, curr = None, head
        while left > 1:
            prev, curr = curr, curr.next
            left -= 1
            right -= 1

        third, con, tail = None, prev, curr
        while right > 0:
            third = curr.next
            curr.next = prev
            prev = curr
            curr = third
            right -= 1
        if con is not None:
            con.next = prev
        else:
            head = prev
        tail.next = curr
        return head

# @lc code=end

if __name__ == "__main__":
    # Example usage:
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    left, right = 2, 4

    solution = Solution()
    new_head = solution.reverseBetween(head, left, right)

    # Print the reversed linked list
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
