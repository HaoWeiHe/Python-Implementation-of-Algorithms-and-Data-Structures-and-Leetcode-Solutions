# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res =[]
        def dfs(root, record, acc):
            if not root:
                return 
           
            if not root.right and not root.left:
                acc += root.val
                
                if acc == sum:
                    
                    self.res.append(record+[root.val])
                return 
            dfs(root.right, record+[root.val],acc+root.val)
            
            dfs(root.left, record + [root.val],acc+root.val)
            
      
        dfs(root, [],0)
        return self.res
        