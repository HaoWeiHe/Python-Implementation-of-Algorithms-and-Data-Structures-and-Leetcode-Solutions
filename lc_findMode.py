# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, val=0, left=None, right=None):
#		 self.val = val
#		 self.left = left
#		 self.right = right
import collections
class Solution(object):
	def findMode(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root: return 0		
		self.dic = collections.defaultdict(int)
		def dfs(root):
			if not root: return 
			self.dic[root.val]+=1
			dfs(root.right)
			dfs(root.left)
		dfs(root)

		_max = 0
		self.tmp = collections.defaultdict(list)
		for k,v in self.dic.items():
			_max = max(_max, v)
			self.tmp[v].append(k)

		return self.tmp[_max]