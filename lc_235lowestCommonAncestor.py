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
        if not root:
            return None
        
        if root in [p,q]:
            return root
        
        lf, rt = self.lowestCommonAncestor(root.left,p,q), self.lowestCommonAncestor(root.right,p,q)
        
        if lf != None and rt!= None:
            return root
        if lf!= None:
            return lf
        if rt!= None:
            return rt
        