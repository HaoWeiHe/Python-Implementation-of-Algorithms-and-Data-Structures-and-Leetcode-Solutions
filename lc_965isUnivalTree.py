# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(r):
            if not r :
                return 1
            if root.val != r.val:
                return 0
            lf = dfs(r.left)
            rt = dfs(r.right)
            return lf and rt and root.val == r.val
        return dfs(root)