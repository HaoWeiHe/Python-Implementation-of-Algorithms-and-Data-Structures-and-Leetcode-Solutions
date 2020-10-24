
# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, val=0, left=None, right=None):
#		 self.val = val
#		 self.left = left
#		 self.right = right
class Solution(object):
	def isValidBST(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		def dfs(root , lower, upper):

			if not root: return 1
			val = root.val
			if val > upper or val < lower: return 0

			if not dfs(root.right, lower,val ): return 0
			if not dfs(root.left, val, upper): return 0
			return 1
		return dfs(root, -float('inf'), float('inf'))
