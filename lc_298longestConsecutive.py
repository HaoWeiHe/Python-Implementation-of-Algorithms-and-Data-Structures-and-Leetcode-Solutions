# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 1
        def dfs(node, preNode, diff, acc):
            if not node:
                return 
          
            cur_diff = node.val - preNode.val
            if cur_diff == 1 and (acc == 1 or diff == cur_diff):
                acc += 1
            else:
                acc = 1
          
            self.ans = max(self.ans, acc)
            dfs(node.right, node, cur_diff, acc)
            dfs(node.left, node, cur_diff, acc)
            
            
        dfs(root, root,0, 0 )
        return self.ans 
        