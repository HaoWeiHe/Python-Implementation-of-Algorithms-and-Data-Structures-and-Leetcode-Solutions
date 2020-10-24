# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.pre = float('inf')
        self.res = float('inf')
        def dfs(node):
            if not node:return 
            dfs(node.left)
            self.res = min(self.res, abs(node.val-self.pre))
            self.pre = node.val
            dfs(node.right)
        dfs(root)
        return self.res