# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(root, val):
          
            if not root:
                return 
            if not root.right and not root.left:
                self.res += val*2 + root.val
                return 
            dfs(root.right, val*2 + root.val)
            dfs(root.left, val*2 + root.val)
        dfs(root, 0)
        return self.res