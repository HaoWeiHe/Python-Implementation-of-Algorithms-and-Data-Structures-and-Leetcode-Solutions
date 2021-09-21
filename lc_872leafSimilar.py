# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        lst1 = []
        def dfs(root):
            if not root:return []
            if not root.right and not root.left:
                return [root.val]
            return dfs(root.left) + dfs(root.right)
        
        lst1 = deque(dfs(root1))
        
        def check(root):
            
            if not root:
                return True
            if not root.right and not root.left:
                if not lst1:return False
                
                return root.val == lst1.popleft()
            return check(root.left) and check(root.right)
        return check(root2) and not lst1