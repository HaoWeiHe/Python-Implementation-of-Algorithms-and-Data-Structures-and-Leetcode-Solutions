# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0 
        def dfs(node):
            if not node:
                return 0
            lf, rt = dfs(node.left), dfs(node.right)
            self.res += abs(lf - rt) 
            return node.val + lf + rt
        dfs(root)
        return self.res