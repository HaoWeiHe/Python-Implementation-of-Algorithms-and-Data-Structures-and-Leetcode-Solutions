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
        def dfs(root):
            if not root:
                return 0, None #acc, pre_node
            if not root.right and not root.left:
                return 1, root
            
            l, prel = dfs(root.left)
            r, prer = dfs(root.right)
            
            if  prel and prel.val == 1 + root.val:
                l += 1
            else:
                l = 1
            if  prer and prer.val == 1 + root.val:
                r += 1
            else:
                r = 1
            self.ans = max(self.ans, r, l)
            return max(r, l), root
        dfs(root)
        return self.ans
class Solution(object):
    def longestConsecutive2(self, root):
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
        