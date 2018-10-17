
class Solution(object):
    
    def binaryTreePaths(self, root):

        res = []
        
        if (not root):
            return []
        
        self.dfs(root,"",res)
        
        return res
        
        
    def dfs(self, root, ls, res):
        
        if(root.left):
            self.dfs(root.left, ls+ str(root.val) +"->", res)
        
        if(root.right):
            self.dfs(root.right, ls + str(root.val) +"->",res)
        
        if(not root.right and not root.left):
            
            return res.append(ls + str(root.val))