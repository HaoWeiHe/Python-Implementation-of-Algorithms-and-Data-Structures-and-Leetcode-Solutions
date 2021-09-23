# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        lst = []
        def dfs(r):
            if not r:
                return 
            lst.append(r.val)
            dfs(r.right)
            dfs(r.left)
        dfs(root)
        lst.sort()
        return min(lst[i] - lst[i-1] for i in range(1,len(lst)))
    def minDiffInBST2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.lst =[]
        self.ans = float("inf")
        def bs(val):
            l, r= 0, len(self.lst)
            while l < r:
                m = l + (r-l)/2
                if self.lst[m] > val:
                    r = m
                else:
                    l = m + 1
            return l
                
        def dfs(root):
            if not root:return 
            insert_idx = bs(root.val)
            self.lst = self.lst[:insert_idx] + [root.val] + self.lst[insert_idx:]
            
            if insert_idx - 1 >= 0 :
                self.ans = min(self.ans, abs(root.val- self.lst[insert_idx - 1] ))
            if insert_idx + 1 < len(self.lst):
                self.ans = min(self.ans, abs(root.val- self.lst[insert_idx + 1] )) 
            dfs(root.right) 
            dfs(root.left)
        dfs(root)
      
        return self.ans
            