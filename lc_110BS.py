# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root):
            if not root:return 0
            L, R = dfs(root.right), dfs(root.left)
            if L == -1 or R == -1:
                return -1
            if abs(L-R) > 1:
                return -1
            return max(L,R) + 1
        return dfs(root) != -1