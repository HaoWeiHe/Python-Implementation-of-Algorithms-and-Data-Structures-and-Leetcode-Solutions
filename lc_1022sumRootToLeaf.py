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
            cur_val = val*2 + root.val
            if not root.right and not root.left:
                self.res += cur_val
                return 
            dfs(root.right, cur_val)
            dfs(root.left, cur_val)
        dfs(root, 0)
        return self.res