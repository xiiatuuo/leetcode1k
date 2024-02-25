#
# @lc app=leetcode.cn id=160 lang=python
#
# [160] 相交链表
#  A + B = B + A

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        pa = headA
        pb = headB

        while pa != pb:
            if not pa:
                pa = headB
            else:
                pa = pa.next
            if not pb:
                pb = headA
            else:
                pb = pb.next
        return pa
