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
        def dfs(root, record, score, lvl):
            if not root:
                return 

            record =  unichr(97 + root.val) + record
           
            if not root.right and not root.left:
                if self.res == "":
                    self.res = record
                if record < self.res:
                    self.res = record
                   
            dfs(root.right, record,score, lvl +1)
            dfs(root.left, record,score, lvl +1)
            
            return root.val
        dfs(root, "", 0,0)
        return self.res
        
        
        
        
        
        
        
            
                