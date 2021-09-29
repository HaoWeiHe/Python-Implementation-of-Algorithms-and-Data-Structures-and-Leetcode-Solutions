# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = []
        def dfs(root):
            if not root:return 
            if -root.val not in self.ans:
                heapq.heappush(self.ans, -root.val)
            if len(self.ans) > 2:
                heapq.heappop(self.ans)
        
            dfs(root.right)
            dfs(root.left)
        dfs(root)
       
        return -self.ans[0] if len(self.ans) == 2 else -1