# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.ans = 1
        
        #if valid_behind and min < cur.val < max : self.ans = max(self.ans, cur.val)
        def dfs(root):
            if not root: #max, min, valid_behind, count
                return float("-inf"),float("inf"), True, 0
            
            if not root.right and not root.left:
                return root.val, root.val,True, 1
            
            rmax, rmin, valid_r, cr = dfs(root.right)
            lmax, lmin, valid_l, cl = dfs(root.left)
            
            if valid_l and valid_r and (lmax < root.val < rmin):
                self.ans = max(self.ans, cr + cl + 1)
                return max(root.val,rmax,lmax), min(root.val,rmin, lmin),True, cr + cl + 1
            return max(root.val,rmax,lmax), min(root.val,rmin, lmin), False,1
        dfs(root)
        return self.ans
            
                