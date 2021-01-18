
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def countDepth(root,right):
            if not root:return 0
            if right:
                return 1+ countDepth(root.right, right)
            else:
                return 1+ countDepth(root.left, right)
        def dfs(root):
            if not root:return 0
            r_dth = countDepth(root.right,1) 
            l_dth = countDepth(root.left,0)
            if r_dth == l_dth :
                return pow(2, r_dth+1)-1
            else:
                return 1 + dfs(root.right) + dfs(root.left)
        return dfs(root)
    def countNodes2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.n  = 0 
        def dfs(r):
            if not r:return 
            self.n +=1
            dfs(r.right)
            dfs(r.left)
        dfs(root)
        return self.n