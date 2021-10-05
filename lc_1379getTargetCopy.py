# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        self.ans = ""
        def dfs(a,b):
            if not a:
                return
            if a == target:
                self.ans = b
            dfs(a.right, b.right)
            dfs(a.left, b.left)
        dfs(original,cloned)
        return self.ans