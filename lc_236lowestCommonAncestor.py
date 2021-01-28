# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def f(n):
            if not n:return 
            if n == p or n == q :return  n
            
            lf,rt = f(n.left),f(n.right)
            if lf and rt:return n
            return lf if lf else rt
        return f(root)