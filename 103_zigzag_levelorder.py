#
# @lc app=leetcode.cn id=103 lang=python
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result_list = []
        queue = [root]
        bool_reversed = False
        while len(queue):
            if not bool_reversed:
                result_list.append([i.val for i in queue])
            else:
                result_list.append(reversed([i.val for i in queue]))
            bool_reversed = ~bool_reversed
            print("result_list=%s" % result_list)
            tmp_queue = []
            for res in queue:
                print("res.value=%s|res.left=%s|res.right=%s" %(res.val,res.left,res.right))
                if  res.left is not None:
                    tmp_queue.append(res.left)
                if  res.right is not None :
                    tmp_queue.append(res.right)
               
            print("bak_queue=%s" %tmp_queue)
            queue = tmp_queue

        return result_list
