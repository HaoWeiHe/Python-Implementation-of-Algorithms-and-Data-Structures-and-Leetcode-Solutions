class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(low, hi, node):
            if not node:return True
            if low < node.val < hi:
                return dfs(low, node.val, node.left) and dfs(node.val, hi, node.right)
            return False
        return dfs(float('-inf'), float('inf'), root)