# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def check(cmp_node, ori_node):
            if not cmp_node and not ori_node:
                return True
            if not ori_node:return False
            if not cmp_node:retrun False
            
            return cmp_node.val == ori_node.val and check(cmp_node.right, ori_node.right) and check(cmp_node.left, ori_node.left)
        
        def runEachNode(root = s):
            if not root:
                return 
            if check(root):
                return True
            runEachNode(root.right)
            runEachNode(root.left)
        return True if runEachNode() else False
            
        