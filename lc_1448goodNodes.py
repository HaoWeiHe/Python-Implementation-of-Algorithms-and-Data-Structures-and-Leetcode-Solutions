# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:return 0
        self.ans = 0
        
        def dfs(root, tmp):
            if not root:return 
            if root.val >= tmp:
                
                self.ans +=1
                
            dfs(root.right, max(tmp, root.val))
            dfs(root.left, max(tmp, root.val))
        dfs(root,root.val)
        return self.ans