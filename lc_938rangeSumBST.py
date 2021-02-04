# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.res = 0
        def dfs(node):
            if not node:return 
           
            if low <= node.val <= high:
                self.res += node.val
            if node.val > high:
                dfs(node.left)
            elif node.val < low:
                dfs(node.right)
            else:
                dfs(node.right)
                dfs(node.left)
        dfs(root)
        return self.res