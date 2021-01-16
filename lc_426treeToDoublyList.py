"""
# Definition for a Node.
class Node(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
"""

class Solution(object):
	def treeToDoublyList(self, root):
		"""
		:type root: Node
		:rtype: Node
		"""
		self.first, self.last = None, None
		if not root:return 
		def dfs(node):
			if not node:return 
			dfs(node.left)
			if not self.first:
				self.first = node
			else:
				self.last.right = node
				node.left = self.last
			self.last = node
			dfs(node.right)
		
		dfs(root)
		self.first.left = self.last
		self.last.right = self.first
		return self.first	