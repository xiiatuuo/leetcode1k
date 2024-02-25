# @lc app=leetcode.cn id=236 lang=python
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ancestor = TreeNode(-1)
        def recursion(node):
            if not node:
                return False

            in_left = recursion(node.left)
            in_right = recursion(node.right)
            if (in_left and in_right) or ((node.val==p.val or node.val==q.val) and (in_left or in_right)):
                ancestor.val = node.val
                ancestor.left = node.left
                ancestor.right = node.right
            return in_left or in_right or node.val==p.val or node.val==q.val

        recursion(root)

        return ancestor
