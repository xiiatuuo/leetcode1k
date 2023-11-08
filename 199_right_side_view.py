class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(node, depth):
            if not node:
                return
            if len(res) == depth:
                res.append(node.val)
            depth = depth + 1
            dfs(node.right, depth)
            dfs(node.left, depth)

        res = []
        dfs(root, 0)
        return res
        
