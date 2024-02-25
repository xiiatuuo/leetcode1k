#
# @lc app=leetcode.cn id=92 lang=python
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy_node = ListNode(-1)
        dummy_node.next = head
        prev = dummy_node
        for _ in xrange(left-1):
            prev = prev.next
        cur = prev.next
        for _ in xrange(right-left):
            next = cur.next
            cur.next = next.next
            next.next = prev.next
            prev.next = next
       
        return dummy_node.next

