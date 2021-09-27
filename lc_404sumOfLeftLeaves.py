# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, left = False):
            if not root:return 0
            if not root.right and not root.left and left:
                return root.val
            lf = dfs(root.left,True)
            rt = dfs(root.right)
            return lf + rt
        return dfs(root)
        