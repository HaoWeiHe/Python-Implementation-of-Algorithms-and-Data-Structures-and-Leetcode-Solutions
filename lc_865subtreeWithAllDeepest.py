# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        d = defaultdict(int)
        def dfs(root, lvl):
            if not root:
                return 
            if not root.right and not root.left:
                d[lvl] += 1
                return 
            dfs(root.right, lvl + 1)
            dfs(root.left, lvl + 1)
        dfs(root, 0)
        deepest = max(d.keys())
        deepest_nu = d[deepest]
        
        def getRoot(root,lvl):
            if not root:
                return root, 0
            if lvl == deepest:
                return root, 1
            
            lf, cl = getRoot(root.left,lvl+ 1)
            paris = getRoot(root.right, lvl + 1)
            rt, cr =  paris
            if cr == deepest_nu:
                return rt, cl + cr
            if cl == deepest_nu:
                return lf, cl + cr
            if cl+ cr == deepest_nu:
                return root, cl + cr

            return root, cl + cr
        return getRoot(root,0)[0]