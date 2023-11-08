# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(node, result):
            if node is None:
                return
            dfs(node.left, result)
            result.append(node.val)
            dfs(node.right, result)

        result = []
        dfs(root, result)
        return result
        
