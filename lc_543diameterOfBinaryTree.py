# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(root):
            if not root:
                return 0
            lf = dfs(root.left)
            rt = dfs(root.right)
            self.res = max(self.res, lf + rt )
            return 1 + max(lf,rt)
        dfs(root)
        return self.res