#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = list1
        if l is not None and list2 is not None:
            if l.val > list2.val:
                tmp = list2
                list2 = list2.next
                tmp.next = l.next
                l.next = tmp
            l = l.next
        if list2 is not None:
            l.next = list2
        return list1
# @lc code=end