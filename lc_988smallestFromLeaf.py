# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.min = float('inf')
        self.res = ""
        def dfs(root, record):
            if not root:
                return 

            record =  unichr(97 + root.val) + record
           
            if not root.right and not root.left:
                if self.res == "":
                    self.res = record
                if record < self.res:
                    self.res = record
                   
            dfs(root.right, record)
            dfs(root.left, record)
            
            return root.val
        dfs(root, "")
        return self.res
        
        
        
        
        
        
        
            
                