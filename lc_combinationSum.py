class Solution(object):

	def combinationSum(self, candidates, target):
		res = []
		candidates.sort()
		def helper(candidates, idx, remain,tmp):
			if remain == 0:
				res.append(tmp)
				return 
			if remain < 0 :
				return 

			for i in range(idx, len(candidates)):
				elem = candidates[i]
				if elem > remain: break

				helper(candidates,i, remain - elem,tmp+[elem])
		
		helper(candidates, 0, target, [])
		return res