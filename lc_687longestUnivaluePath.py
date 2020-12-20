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
        def dfs(root):
            if not root:
                return None, 0
                
            lf_val , lf_freq = dfs(root.left)
            rt_val, rt_freq = dfs(root.right)
            cur_freq, right_left = 0, 0 
            if lf_val == root.val:
                cur_freq += lf_freq
                right_left = lf_freq
            if rt_val == root.val:
                cur_freq += rt_freq
                right_left = max(right_left, rt_freq)
            
            self.res = max(self.res, cur_freq )
            return root.val, right_left + 1
        dfs(root)
        return self.res
    
    
    
    
    
    
    