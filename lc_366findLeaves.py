# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d = collections.defaultdict(list)
        def dfs(root):
            if not root:
                return 0
            lf = dfs(root.left) +1 
            rt = dfs(root.right) + 1
            lvl = max(lf, rt)
            d[lvl].append(root.val)
            
            return lvl
        
        dfs(root)
        return [d[r] for r in range(1, len(d)+1)]