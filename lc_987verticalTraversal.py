# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.d = collections.defaultdict(list)
        
        def dfs(root, col, row):
            if not root:
                return 
            self.d[col].append((root.val, row))   
            
            
            dfs(root.left,  col -1, row +1) or dfs(root.right, col+1, row + 1)
            
        dfs(root, 0,0)
        res =[]
       
        for k in sorted(self.d.keys()):
            tmp = [e[0] for e in sorted(self.d[k], key = lambda x: (x[1],x[0]))]
            res.append(tmp)
        
        return res