# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:return 0
        def dfs(root):
     
            if root:
                if not root.right and not root.left:
                    return 1
                l = dfs(root.left) 
                r = dfs(root.right)
                return min(l if l else float("inf"), r if r else float("inf") ) + 1
        return dfs(root)
            
        