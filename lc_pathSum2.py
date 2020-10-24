# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        
        res = []
        final = []
        
        
        if (not root):
            return []
        
        self.dfs(root,"",res)
  
        
        for m in res:
            eles = m.split(">")
            eles = map(int,eles)
            summary = 0 
            for ele in eles:
                summary += ele
            if summary == sum:
                final.append(eles)
            
            # # if sum(map(int,ele)) == sum:
            # #     final.append(map(int,ele))
            # for els in eles:
            #     a +=int(els)
            # if a == sum:
            #     final.append(eles)
    
        return final
        
        
    def dfs(self, root, ls, res):
        
        if(root.left):
            self.dfs(root.left, ls+ str(root.val) +">", res)
        
        if(root.right):
            self.dfs(root.right, ls + str(root.val) +">",res)
        
        if(not root.right and not root.left):
            
            return res.append(ls + str(root.val))
      