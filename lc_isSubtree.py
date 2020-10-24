
class Solution(object):
	def isSubtree(self, s, t):
		"""
		:type s: TreeNode
		:type t: TreeNode
		:rtype: bool
		"""
		def dfs(t1,t2):
			if not t1:return
			if t1.val ==t2.val :
				return t1
			r = dfs(t1.right,t2)
			l = dfs(t1.left,t2)
			return r if r else l
			
		
		def isMatch(self, s, t):
			if not(s and t):
				return s is t
			return (s.val == t.val and 
					self.isMatch(s.left, t.left) and 
					self.isMatch(s.right, t.right))

		start = dfs(s,t)
		
		return cmp(start, t)
			
		

