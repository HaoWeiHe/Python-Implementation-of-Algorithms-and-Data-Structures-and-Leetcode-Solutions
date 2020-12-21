
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = []
        def dfs(root,num):
            if not root:return 
            num = num * 10 + root.val
            if not root.right and not root.left:
                self.res.append(num)
                return 
            dfs(root.right,num)
            dfs(root.left,num)
        dfs(root, 0)
        return sum(self.res)