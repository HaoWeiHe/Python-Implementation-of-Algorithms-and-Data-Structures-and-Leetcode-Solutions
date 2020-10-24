import collections
class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		d = { ")" :"(", "]":"[","}":"{"}
		lst = []
		for elem in s:
			if elem in d:
				if  len(lst) == 0 or lst.pop() != d[elem]:
					return False						
			else:
				lst.append(elem)

		return False if lst else True


s =  "]"
print(Solution().isValid(s))