# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node: return None
            if not node.right and not node.left: return node
            lf_tail = dfs(node.left)
            rt_tail = dfs(node.right)
            if lf_tail:
                lf_tail.right = node.right
                node.right = node.left
                node.left = None
            
            return rt_tail if rt_tail else lf_tail
        dfs(root)