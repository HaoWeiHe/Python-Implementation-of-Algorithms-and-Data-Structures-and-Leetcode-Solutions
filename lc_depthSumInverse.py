
class Solution(object):
	def depthSum(self, nestedList):
		"""
		:type nestedList: List[NestedInteger]
		:rtype: int
		"""
		# [1,[4,[6]]]
		self.res = 0
		def dfs(lev, lst):
			# print(lst)
			for ele in lst:
				if ele.isInteger():
					self.res += lev * ele.getInteger()
				else:
					dfs(lev+1, ee)
		
		dfs(1,nestedList)
		return self.res
