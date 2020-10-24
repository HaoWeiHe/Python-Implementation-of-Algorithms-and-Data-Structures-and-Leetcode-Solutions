
class Solution(object):
	def depthSumInverse(self, nestedList):
		"""
		:type nestedList: List[NestedInteger]
		:rtype: int
		"""
		res,unweight  = 0,0

		while nestedList:
			subList = []
			
			for ele in nestedList:
				if ele.isInteger():
					unweight += ele.getInteger() #11
				else:
					subList.extend(ele.getList()) #[[6]]
			res += unweight #res = 1 +5 + 11
			nestedList = subList
		return res

[1,[4,[6]]] 
1, 
1+4
1+4+6
[[1,1],2,[1,1]]