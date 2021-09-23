# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def cmp(p,q):
            if p and not q:
                return False
            if q and not p:
                return False
            if not p and not q:
                return True
            return p.val == q.val and cmp(p.right, q.right) and cmp(p.left, q.left)
        return cmp(p,q)