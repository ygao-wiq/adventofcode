#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# from typing import Optional, List

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        total_lists = len(lists)
        interval = 1
        while interval < total_lists:
            i = 0
            while i+interval<total_lists:
                lists[i] = self.mergeTwoLists(lists[i], lists[i+interval])
                i += interval*2
            interval = interval * 2
        return lists[0] if lists else None
        
# @lc code=end
# def convert_list_to_list_node(l: list[int]) -> Optional[ListNode]:
#     dummy_head = ListNode(-1, None)
#     current = dummy_head
#     for e in l:
#         current.next = ListNode(e, None)
#         current = current.next
#     return dummy_head.next

# def convert_list_node_to_list(ln: Optional[ListNode]) -> list[int]:
#     ret = list()
#     while ln:
#         ret.append(ln.val)
#         ln = ln.next
#     return ret
    
# if __name__ == "__main__":
#     lists = list()
#     for l in [[1,4,5],[1,3,4],[2,6]]:
#         lists.append(convert_list_to_list_node(l))
#     print(convert_list_node_to_list(Solution().mergeKLists(lists)))