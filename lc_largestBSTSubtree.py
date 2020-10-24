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
        self.res = 0
        def dfs(node):
            if not node:
                return 0,float('inf'), -float('inf')
        
            n1, min1, max1 = dfs(node.left)
            n2, min2, max2 = dfs(node.right)
            n = n1 + n2 + 1 if max1 < node.val < min2 else float('-inf')
            self.res = max(self.res, n)
            return n, min(node.val, min1), max(node.val, max2)
        dfs(root)
        return self.res
                

def largestBSTSubtree(self, root):
    def dfs(root):
        if not root:
            return 0, 0, float('inf'), float('-inf')
        N1, n1, min1, max1 = dfs(root.left)
        N2, n2, min2, max2 = dfs(root.right)
        n = n1 + 1 + n2 if max1 < root.val < min2 else float('-inf')
        return max(N1, N2, n), n, min(min1, root.val), max(max2, root.val)
    return dfs(root)[0]
