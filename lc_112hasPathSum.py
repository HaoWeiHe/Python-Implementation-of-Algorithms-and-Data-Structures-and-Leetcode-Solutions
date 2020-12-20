
class Solution(object):
    def hasPathSum(self, root, sum):
     
        if not root:
            return False
        
        def dfs(root,acc):
            if not root:return False
            if not root.right and not root.left:
                return (acc + root.val) == sum
            
            return dfs(root.right, acc + root.val) or dfs(root.left, acc + root.val)
        return dfs(root,0)
            