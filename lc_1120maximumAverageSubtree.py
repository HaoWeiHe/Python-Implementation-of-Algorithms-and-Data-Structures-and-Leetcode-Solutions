# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        self.res = 0
        def dfs(root):
            if not root:
                return 0,0
            lc, lv = dfs(root.left)
            rc, rv = dfs(root.right)
            value, count = lv + rv + root.val, lc + rc + 1 
            self.res = max(self.res, value/ float(count))
            return count, value
        dfs(root)
        return self.res