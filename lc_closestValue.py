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
        res = root.val
        
        while root:
            
            if not root: return res
            
            if abs(root.val - target) < abs(res-target):
                res = root.val
            if root.val == target: return 0
            if  root.val > target: root = root.left
            if root.val < target: root = root.right
            
        return res