# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        
        def dfs(root):
            if not root:
                return ""
            if not root.right and not root.left :
                return str(root.val)
            if not root.right:
                return str(root.val) + "(" + dfs(root.left) + ")" 
            return str(root.val) + "(" + dfs(root.left) + ")(" + dfs(root.right) + ")"
        return dfs(root)
    def tree2str2(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.res = []
        def dfs(root):
            if not root:
                return []
            if not root.right and not root.left :
                return [str(root.val)] 
            if not root.right:
                return [str(root.val)] + ["("] + dfs(root.left) + [")"] 
            return [str(root.val)] + ["("] + dfs(root.left) + [")"] + ["("] + dfs(root.right) + [")"] 
        return "".join(dfs(root))