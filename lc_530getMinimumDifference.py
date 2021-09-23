# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        [4,2,6,1,3]
        [1,2,3,4,6]
           1 1  1 2
    ans    1  1  1 1
        """
        
        def dfs(root):
            if not root:
                return []
            return dfs(root.left) + [root.val] + dfs(root.right)
        lst = sorted(dfs(root))
        ans = float("inf")
        for i in range(1, len(lst)):
            ans = min(ans, lst[i] - lst[i-1])
        return ans