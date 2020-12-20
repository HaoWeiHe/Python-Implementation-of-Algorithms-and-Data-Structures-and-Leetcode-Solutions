# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res  = float('-inf')
        def dfs(root):
            if not root:return 0
            l = max(0, dfs(root.left))
            r = max(0,dfs(root.right))
            cur_max = root.val + l + r
            self.res = max(self.res, cur_max)
            return root.val + max(l,r,0)
        dfs(root)
        return self.res