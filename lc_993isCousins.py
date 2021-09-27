# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        self.xlvl, self.ylvl = (0,None),(0,None)
        def traverse(root, d,p):
            if not root:
                return 
            
            if root.val == x :
                self.xlvl = (d,p.val)
                 
            if root.val == y :
                self.ylvl = (d,p.val)
                 
            traverse(root.right, d + 1,root)
            traverse(root.left, d + 1, root)
        traverse(root, 0,root)
       
        return self.xlvl[0] == self.ylvl[0] and self.xlvl[1] != self.ylvl[1]