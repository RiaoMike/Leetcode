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
# @lc code=end

        index1 = 0
        index2 = 0
        while index1 < len(list1) and index2 < len(list2):
            if list2[index2] >= list1[index1]:
                index1 += 1
            else:
                list1.insert(index1, list2[index2])
                index2 += 1
                index1 += 1
        list1 = list1 + list2[index2:]
        return list1


