# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
   
    def hasPathSum(self, root, sum):
        if not root : 
            return False
        
        
        if ((not root.right) and (not root.left)): 
            
            if (root.val == sum):
                
                return True
            else:
                return False
                
        
        if(self.hasPathSum(root.left, sum-root.val )):
            
            return True
        
        
        if(self.hasPathSum(root.right, sum-root.val)):
            
            return True
        
        return False
            
    