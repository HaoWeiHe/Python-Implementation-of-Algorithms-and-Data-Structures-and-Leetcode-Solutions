# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def h(self,root):
            if not root :return 0
            rt = self.h(root.right)
            lf = self.h(root.left)
            return max(rt, lf) +1
        
    def isBalanced(self, root ):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def dfs(root):
            if not root: return True
            rt =self.h(root.right)
            lf = self.h(root.left)
            
            return abs(rt - lf) < 2 and dfs(root.right) and dfs(root.left)
        return dfs(root)
        