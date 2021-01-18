# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        
        self.res = float('inf')
        self.dis = float('inf')
        def dfs(root):
            if not root:return 
            if self.dis > (abs(target - root.val)):
                self.dis = abs(target - root.val)
                self.res = root.val
            
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.res