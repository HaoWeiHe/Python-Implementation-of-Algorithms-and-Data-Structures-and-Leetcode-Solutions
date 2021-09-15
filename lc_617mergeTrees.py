# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees2(self, r1, r2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not r1 and not r2:
            return 
        
        root = TreeNode((r1.val if r1 else 0 ) + (r2.val if r2 else 0))
 
      
            
        root.left =  self.mergeTrees(r1.left if r1 else None, r2.left if r2 else None)
        root.right = self.mergeTrees(r1.right if r1 else None, r2.right if r2 else None)
        return root
class Solution(object):
    def mergeTrees(self, r1, r2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not r1 and not r2:
            return 
        if not r2:
            r2 = TreeNode(0)
        if not r1:
            r1 = TreeNode(0)
        root = TreeNode(r1.val + r2.val)
        root.left =  self.mergeTrees(r1.left, r2.left)
        root.right = self.mergeTrees(r1.right, r2.right)
        return root