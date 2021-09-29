# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans, self.d = [], 0
        
        def dfs(root, deep, s):
            if not root:return 
            if not root.right and not root.left:
                if deep > self.d:
                    self.d = deep
                    self.ans = [root.val]
                    return 
                if deep == self.d:
                    self.ans.append(root.val)
                    return 
            dfs(root.right, deep + 1, s + root.val)
            dfs(root.left, deep + 1, s + root.val)
        dfs(root, 0, 0 )
       
        return sum(self.ans)