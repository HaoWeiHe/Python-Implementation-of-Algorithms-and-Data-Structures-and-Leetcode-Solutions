# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
    
#     def hight(self,root):
#         if not root:
#             return 0 
        
#         return max(self.hight(root.left), self.hight(root.right)) +1
        
#     def diameterOfBinaryTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if not root:
#             return 0
        
#         rightHeight, leftHeight = 0, 0 
        
#         if not rightHeight:
#             rightHeight = self.hight(root.right)
#         if not leftHeight:
#             leftHeight = self.hight(root.left)
        
#         rdiameter = self.diameterOfBinaryTree(root.right)
#         ldiameter = self.diameterOfBinaryTree(root.left)
        
#         return max(rightHeight + leftHeight + 1, max(rdiameter, ldiameter)+1 ) -1
        
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1