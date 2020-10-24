class Solution(object):
	def minSteps(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n <2: return 0
		def helper(n):
			factors = []
			if n <=1 : return 0
			# print(n)
			res = float('inf')
			for i in range(1,n):
				a,b = divmod(n,i)
				if b ==0:
					factors.append((i,a))

			for dp_ele, timefactor in factors:
				res = min(res, helper(dp_ele)+1+(timefactor-1))
			return res

		return helper(n)

# 3*5
# A copy
# AA paste
# AAA paste
# AAA copy
# AAAAAA paste


# a
# aa -> 1*2 -> copy past-> 
# aaa -> 3
# aaaa
print(Solution().minSteps(100),"w")