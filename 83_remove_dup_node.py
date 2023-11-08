class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        cur = head

        while cur and cur.next:
            move_flag = False
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
                move_flag = True
            if move_flag:
                pre.next = cur.next
            else:
                pre.next = cur
                pre = cur
            cur = cur.next

        return dummy.next
