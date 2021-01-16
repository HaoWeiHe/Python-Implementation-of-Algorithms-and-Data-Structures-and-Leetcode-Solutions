# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        d = collections.defaultdict(list)
        def dfs(lvl, node, top):
            if not node:return 
            d[lvl].append((node.val, top))
            dfs(lvl -1, node.left, top + 1)
            dfs(lvl + 1, node.right, top + 1)
            
        dfs(0, root,0)
        res = []
 
        for lvl in range(min(d), max(d)+1):
            if lvl not in d: continue
            res.append([x[0] for x in sorted(d[lvl], key  = lambda x: x[1])])
        return res
        