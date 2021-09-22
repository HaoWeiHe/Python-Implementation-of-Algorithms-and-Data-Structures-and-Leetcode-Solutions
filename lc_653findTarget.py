# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, target):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        h = set()
        def dfs(root):
            if not root:
                return False
            if root.val in h:
                return True
            h.add(target - root.val)
            lf = dfs(root.left)
            rt = dfs(root.right)
            
            return True if lf or rt else False
        return dfs(root)