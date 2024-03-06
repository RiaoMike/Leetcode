#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = None
        tail = None
        while l2 is not None or l1 is not None:
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0
            sum = v1 + v2 + carry
            carry = sum // 10
            if head is None:
                head = ListNode(sum % 10, None)
                tail = head
            else:
                tail.next = ListNode(sum % 10, None)
                tail = tail.next
            if l1 is not None:
                l1 = l1.next;
            if l2 is not None:
                l2 = l2.next
        if carry == 1:
            tail.next = ListNode(1, None)
        return head

# @lc code=end 

