# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ans = self.cur = TreeNode(None)
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            node.left = None
            self.cur.right = node
            self.cur = node
            dfs(node.right)
        dfs(root)
        return ans.right