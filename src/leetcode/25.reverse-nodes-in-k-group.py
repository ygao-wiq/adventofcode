from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1, None)
        current_head = dummy_head
        if k <= 1:
            return head
        i = 0
        temp_head = ListNode(-1, None)
        ret_tail = temp_head.next
        while head:
            temp_head = ListNode(-1, None)
            current = temp_head
            i = 0
            while head and i<k:
                if i == 0:
                    tail = head
                temp = head.next
                head.next = current.next
                current.next = head
                head = temp
                i += 1
            if i == k:
                current_head.next = temp_head.next
                current_head = tail
                ret_tail = tail
        if i<k:
            current = temp_head.next
            while current:
                temp = current.next
                current.next = ret_tail.next
                ret_tail.next = current
                current = temp

        return dummy_head.next

# @lc code=end

def convert_list_to_list_node(l: list[int]) -> Optional[ListNode]:
    dummy_head = ListNode(-1, None)
    current = dummy_head
    for e in l:
        current.next = ListNode(e, None)
        current = current.next
    return dummy_head.next

def convert_list_node_to_list(ln: Optional[ListNode]) -> list[int]:
    ret = list()
    while ln:
        ret.append(ln.val)
        ln = ln.next
    return ret
    
if __name__ == "__main__":
    print(convert_list_node_to_list(Solution().reverseKGroup(convert_list_to_list_node([1,2,3,4,5]), 5)))