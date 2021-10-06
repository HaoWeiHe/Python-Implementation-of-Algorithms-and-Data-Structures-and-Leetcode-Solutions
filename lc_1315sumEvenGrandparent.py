# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0 
        def dfs(root,path):
            if not root:
                return
            if len(path) ==2:
                top = path.pop(0)
                if top%2 ==0:
                    self.ans += root.val
           
            dfs(root.right, path +[root.val])
            dfs(root.left, path + [root.val])
        dfs(root, [])
        return self.ans