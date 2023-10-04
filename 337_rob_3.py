#
# @lc app=leetcode.cn id=337 lang=python
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        g = {}
        f = {}
        g[None] = 0
        f[None] = 0
       
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            f[node] = node.val + g[node.left] + g[node.right]
            g[node] = max(g[node.left], f[node.left]) + max(g[node.right], f[node.right])
        dfs(root)
        return max(g[root],f[root])
