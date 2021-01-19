# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        def dfs(root):
            if not root:
                return TreeNode(val)
            if val > root.val:
                root.right = dfs(root.right)
            else:
                root.left = dfs(root.left)
            return root
        return dfs(root)