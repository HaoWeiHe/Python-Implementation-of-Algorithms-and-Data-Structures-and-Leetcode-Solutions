# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def getList(root):
            if not root:
                return []
            return getList(root.right) + [root.val] + getList(root.left)
        lst = getList(root)
        lst.sort()
        
        def dfs(lst):
            if not lst:
                return None
            
            mid = len(lst)/2
            root = TreeNode(lst[mid])
            
            root.right = dfs(lst[mid+1:])
            root.left = dfs(lst[:mid])
            return root
        return dfs(lst)