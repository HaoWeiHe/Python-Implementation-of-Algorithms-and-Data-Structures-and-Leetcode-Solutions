# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:return 0
        self.ans = 0 
        def dfs(root, prev, acc):
            if not root:
                return 
            acc = 1 if root.val != prev + 1 else acc+1
            self.ans = max(self.ans, acc)
           
       
            dfs(root.right, root.val, acc)
            dfs(root.left, root.val, acc)
        dfs(root, root.val, 1)
        return self.ans