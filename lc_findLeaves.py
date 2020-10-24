

class Solution(object):
	def findLeaves(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		d = collections.defaultdict(list)
		def shake(node):
			if not node: return 0
			if not node.right and not node.left: lvl =  1
			else: lvl = max(shake(node.right) , shake(node.left)) + 1
			d[lvl].append(node.val)
			return lvl

		shake(root)
		return d.values()