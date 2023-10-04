# [141] 环形链表
#  xt: head有可能为空，这是个小坑，或者while改一下

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next
            if  fast == slow:
                return True
        return False

