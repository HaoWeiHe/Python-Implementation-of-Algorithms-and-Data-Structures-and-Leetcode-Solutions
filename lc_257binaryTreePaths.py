# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        def dfs(root, path):
            if not root:
                return 
            path += str(root.val)
            if not root.right and not root.left:
                self.res.append(path)
                return 
            else:
                path += "->"
                dfs(root.left,path)
                dfs(root.right, path)
        
        self.res = []
        dfs(root,"")
        return self.res