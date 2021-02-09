class Solution(object):
	def maximumSwap(self, num):
		"""
		:type num: int
		:rtype: int
		"""
		
		A = map(int, str(num))
		h = {v:i for i,v in enumerate(A)}
		for i, v in enumerate(A):
			for e in xrange(9,v,-1):
				target_idx = h.get(e)
				if target_idx > i:
					A[target_idx], A[i] = A[i], A[target_idx]
					return int("".join(map(str,A)))
		return num
    
    
