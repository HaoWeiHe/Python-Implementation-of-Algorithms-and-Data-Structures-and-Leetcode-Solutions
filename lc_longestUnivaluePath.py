
# class Solution(object):
#     def longestUnivaluePath(self, root):
#         self.ans = 0

#         def arrow_length(node):
#             if not node: return 0
#             lf = arrow_length(node.left)
#             rt = arrow_length(node.right)
            
#             pl, lr = 0,0
#             if node.left and node.left.val == node.val:
#                 pl = lf + 1
#             if node.right and node.right.val == node.val:
#                 lr = rt + 1
            
#             self.ans = max(self.ans, pl + lr)
#             return max(pl ,lr)

#         arrow_length(root)
#         return self.ans





# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(node):
            if not node: return TreeNode(None),0
            if not node.right and not node.left:
                return node, 0
            
            l,r = 0,0
            lfnode, lh = dfs(node.right)
            rtnode, rh = dfs(node.left)
            
            if node.val == lfnode.val:
                l +=  lh +1
            if node.val == rtnode.val:
                r += rh +1
            self.res = max(self.res, l+r)
            return node, max(l,r)
        dfs(root)
            
        return self.res
