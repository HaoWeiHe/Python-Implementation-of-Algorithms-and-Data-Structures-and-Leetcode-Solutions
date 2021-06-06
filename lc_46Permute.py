class Solution(object):
	def permute(self, s):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		"""
		f(abc) = [a + f(bc), b + f(ac) , c + f(ab))
		f(ab) = [a+f(b), b + f(a)]
		f(b) = [s]
		"""
		
		if len(s) == 1:
			return [s]
        
		res = []
		
		for i, v in enumerate(s):
			res.extend([ ele+[v] for ele in self.permute(s[:i] + s[i+1:]) ])
		return res