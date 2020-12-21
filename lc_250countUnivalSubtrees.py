# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countUnivalSubtrees(self, root):
        """
         cmp lf.val == cur and rt.val == cur and rt_his is true, lf_his is ture
        return cur.val, cur.val == val 
        """
        self.res = 0
        
        def dfs(root):
            if not root:
                return None, True
            
            if not root.right and not root.left:
                self.res += 1
                return  root.val, True
            
            lf_val, h1 = dfs(root.left)
            rt_val, h2 = dfs(root.right)
            if lf_val == None:
                lf_val = root.val
            if rt_val == None:
                rt_val = root.val
            cur_his = lf_val == root.val == rt_val and h1 and h2
            if cur_his:
                self.res += 1
            return root.val, cur_his

        dfs(root)
        return self.res