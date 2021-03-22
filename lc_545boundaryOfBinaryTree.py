# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]a
        """
        r, l, lf = [], [], []
        def left(node):
            if not node:return 
            if not node.right and not node.left:
                return 
            l.append(node.val)
            if node.left:
                left(node.left)
            else:
                left(node.right)
        
        def leaves(node):
            if not node:
                return 
            if not node.right and not node.left:
                lf.append(node.val)
                return 
            leaves(node.left)
            leaves(node.right)
        
        def right(node):
            if not node:
                return 
            if not node.right and not node.left:
                return 
            
            r.append(node.val)
            if node.right:
                right(node.right)
            else:
                right(node.left)
        
        left(root.left)
        right(root.right)
        leaves(root.left)
        leaves(root.right)
        
        return [root.val] + l+ lf + r[::-1]
